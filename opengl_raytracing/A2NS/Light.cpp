#include "Light.h"

Light::Light()
{
	colour = glm::vec3(1.0f, 1.0f, 1.0f);
	ambientIntensity = 1.0f;
	diffuseIntensity = 0.0f;
}

Light::Light(GLuint shadowWidth, GLuint shadowHeight, GLfloat red, GLfloat green, GLfloat blue, GLfloat aIntensity, GLfloat dIntensity)
{
	colour = glm::vec3(red, green, blue);
	ambientIntensity = aIntensity;
	diffuseIntensity = dIntensity;

	shadowMap = new ShadowMap();
	shadowMap->Init(shadowWidth, shadowHeight);
}

/*
void Light::keyControl(bool* keys)
{
	// Turn lights on/off
	if (keys[GLFW_KEY_L])
	{
		
	}

	// Decrease ambient lighting
	if (keys[GLFW_KEY_LEFT_BRACKET])
	{

	}

	// Increase ambient lighting
	if (keys[GLFW_KEY_RIGHT_BRACKET])
	{

	}

	// Decrease Diffuse lighting
	if (keys[GLFW_KEY_COMMA])
	{

	}

	// Increase Diffuse lighting
	if (keys[GLFW_KEY_PERIOD])
	{

	}
}
*/

Light::~Light()
{
}
