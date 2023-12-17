#version 450 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;
in vec4 shadowCoord;

struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;
uniform sampler2DShadow shadowMap;
uniform vec2 u_resolution;

float lookUp(float ox, float oy){
    vec2 pixeloffset = 1 / u_resolution;
    return textureProj(shadowMap, shadowCoord + vec4(ox * pixeloffset.x * shadowCoord.w, oy * pixeloffset.y * shadowCoord.w, 0.0, 0.0));
}

float getSoftShadowX16() {
    float shadow;
    float swidth = 1.0;
    float endp = swidth * 1.5;
    for (float y = -endp; y <= endp; y += swidth) {
        for (float x = -endp; x <= endp; x += swidth) {
            shadow += lookUp(x, y);
        }
    }
    return shadow * 0.0625;
}

float getShadow() {
    float shadow = textureProj(shadowMap, shadowCoord);
    return shadow;
}

vec3 getLight(vec3 color) {
    vec3 Normal = normalize(normal);

    //ambient
    vec3 ambient = light.Ia;

    //diffuse
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    //specular
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.Is;

    //shadow
    float shadow = getSoftShadowX16();
    vec3 brightness = (ambient + (diffuse + specular) * shadow);

    return color * brightness;
}

float pow2Exp(float f, int i) {
    for (int j = 0; j <= i; ++j) {
        f *= f;
    }
    return f;
}

float powint(float f, int i) {
    float result = f;
    for (int j = 0; j <= i; ++j) {
        result *= f;
    }
    return result;
}

vec3 getToonLight(vec3 color) {
    vec3 Normal = normal;

    //diffuse
    vec3 lightDir = light.position - fragPos;
    float diff = max(0, dot(lightDir, Normal)) * dot(lightDir, Normal) * dot(light.Id, vec3(0.33333, 0.33333, 0.33333));
    float diffOne = dot(lightDir, lightDir) * dot(Normal, Normal) * dot(light.Id, vec3(0.33333, 0.33333, 0.33333));
    //diff = (diff > diffOne * 0.9)? 1 : (diff > diffOne * 0.4)? 0.95 : (diff > diffOne * 0)? 0.65 : 0;

    //specular
    vec3 viewDir = camPos - fragPos;
    vec3 reflectDir = reflect(-lightDir, Normal);
    int smoothness = 0;
    float spec = pow2Exp(max(dot(viewDir, reflectDir), 0), smoothness + 1) * dot(light.Is, vec3(0.33333, 0.33333, 0.33333));
    float specOne = pow2Exp(dot(viewDir, viewDir) * dot(reflectDir, reflectDir), smoothness) * dot(light.Is, vec3(0.33333, 0.33333, 0.33333));
    //spec = (spec > specOne * 0.9 )? 1 : (spec > specOne * 0.4 )? 0.95 : (spec > specOne * 0 )? 0.65 : 0;

    spec *= diffOne;
    diff *= specOne;
    float diffSpec = spec + diff;
    float diffSpecTwo = diffOne * specOne * 2;

    diffSpec = (diffSpec > diffSpecTwo * 0.9)? 1 : (diffSpec > diffSpecTwo * 0.4)? 0.95 : (diffSpec > 0)? 0.65 : 0;

    //shadow
    float shadow = sqrt(getSoftShadowX16());

    vec3 diffSpecColor = (light.Id + light.Is) * 0.5;

    vec3 tooned = ((diffSpec) * diffSpecColor) * shadow;
    vec3 brightness = (light.Ia + tooned);

    return color * brightness;
}

void main() {
    vec3 color = texture(u_texture_0, uv_0).rgb;

    color = getToonLight(color);

    fragColor = vec4(color, 1.0);
}