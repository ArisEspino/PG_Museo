#version 330 core

layout (location = 0) out vec4 fragColor;

void main()
{
    vec3 color = vec3(0, 1, 1);
    fragColor = vec4(color,1.0);

}