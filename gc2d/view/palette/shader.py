from pyqtgraph.opengl.shaders import FragmentShader, ShaderProgram, VertexShader


class PaletteShader(ShaderProgram):

    def __init__(self, lower_bound, upper_bound, palette):
        """
        This is a custom height shader that will shade the graph based on the supplied palette and bounds.
        :param lower_bound: The lowest point of the shading. Points below this will be the lowest color.
        :param upper_bound: The highest point of the shading. Points above this will be the highest color.
        :param palette: The palette to use.
        """
        palette = palette.getColors('float')

        data = [lower_bound, upper_bound, len(palette)]
        for color in palette:
            data.extend(color)

        super().__init__('palette', [
            VertexShader("""
                            varying vec4 pos;
                            void main() {
                                gl_FrontColor = gl_Color;
                                gl_BackColor = gl_Color;
                                pos = gl_Vertex;
                                gl_Position = ftransform();
                            }
                        """),
            FragmentShader("""
                            #version 140
                            uniform float data[96];
                            
                            varying vec4 pos;
                            //out vec4 gl_FragColor;   // only needed for later glsl versions
                            //in vec4 gl_Color;
                            
                            vec4 getColor(float index){
                                vec4 color = gl_Color;
                                color.x = data[3 + 3*int(index) + 0];
                                color.y = data[3 + 3*int(index) + 1];
                                color.z = data[3 + 3*int(index) + 2];
                                color.w = 1.0;
                                return color;
                            }
                            void main() {
                                vec4 color;
                                if(pos.z <= data[0]){
                                    color = getColor(0);
                                }else if(pos.z > data[1]){
                                    color = getColor(data[2]-1);
                                }else{
                                    float z = (pos.z - data[0]);
                                    float perc = z/ ((data[1]-data[0])/(data[2]-1));
                                    int index = int(perc);
                                    perc = perc-index;
                                    
                                    vec4 a = getColor(index);
                                    vec4 b = getColor(index+1);
                                    color = gl_Color;
                                    
                                    color.x = a.x + perc * ( b.x - a.x);
                                    color.y = a.y + perc * ( b.y - a.y);
                                    color.z = a.z + perc * ( b.z - a.z);
                                }
                                color.w = 1.0;
                                gl_FragColor = color;
                            }
                        """),
        ], uniforms={'data': data})
