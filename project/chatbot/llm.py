import time
from transformers import AutoModelForCausalLM, AutoTokenizer, TextGenerationPipeline
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token

# Loading a pre-trained DialoGPT model from Hugging Face's model hub
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize the text generation pipeline with the model and tokenizer
chatbot = TextGenerationPipeline(model=model, tokenizer=tokenizer, framework="pt")

# Base responses for common questions, stored in a dictionary for quick retrieval
knowledge_base = {
    "conveyor": "For your Conveyor, please ensure you are compliant with the following instructions:\n\n1. Belt Alignment: Regularly check and adjust the belt alignment.\n2. Roller Function: Inspect rollers for smooth operation and replace if necessary.\n3. Motor and Gearbox: Monitor for unusual noises or vibrations and perform routine maintenance.\n4. Conveyor Speed: Verify the conveyor is operating at the correct speed.\n5. Cleaning and Lubrication: Keep the conveyor clean and lubricate moving parts as required.",
    "hello": "Welcome to the Honeywell Generative AI System! How may I assist you today?",
    "pump 3": "If the pump has too much pressure, introduce a coolant.",
    "your name": "I am the Honeywell Chat Bot, and I am here to assist with any of your queries.",
    "filtration": "For your Filtration System, please ensure you are compliant with the following instructions:\n\n1. Filter Integrity: Regularly inspect filters for wear or damage, and replace if necessary.\n2. Flow Monitoring: Check the flow rate to ensure it is within the system's operational range.\n3. Pressure Gauges: Verify pressure levels before and after the filtration process.\n4. Seals and Gaskets: Inspect for leaks or wear and replace as needed.\n5. System Cleaning: Perform routine cleaning to prevent debris build-up.\n6. Sensor Checks: Test all related alarms and sensors for accurate operation.",
    "my role": "You are an engineer at Honeywell.",
    "hey": "Welcome to the Honeywell Generative AI System! How may I assist you today?",
    "heat exchanger": "For your Heat Exchanger, please ensure you are compliant with the following instructions:\n\n1. Temperature Readings: Monitor inlet and outlet temperature readings to ensure proper heat transfer.\n2. Leak Detection: Inspect for leaks and address any issues immediately.\n3. Pressure Drop: Check for unusual pressure drops that could indicate clogging or fouling.\n4. Surface Inspection: Regularly clean and inspect the heat transfer surfaces.\n5. Gasket Condition: Examine and replace worn or damaged gaskets to maintain integrity.",
    "how many reactors": "There are currently three reactors running low on fuel rods.",
    "distributed control": "For your DCS, please ensure you are compliant with the following instructions:\n\n1. Backup Status: Verify the status of automated backup systems and ensure they are functioning correctly.\n2. Power Supply: Monitor power supply voltage levels and ensure they are within specified ranges.\n3. Software Updates: Check for software updates or patches released by the DCS manufacturer and schedule any necessary updates.\n4. Battery Backup: Test and replace backup batteries for critical DCS components if necessary.\n5. Redundancy Testing: Test the redundancy setup to ensure seamless failover in case of hardware or software failures.", 
    "incidence report": "FILLER WORK",
    "what are you": "I am the Honeywell Chat Bot, and I am here to assist with any of your queries.",
    "control valve": "For your Control Valve, please ensure you are compliant with the following instructions:\n\n1. Actuator Function: Test the actuator for proper operation and response.\n2. Stem Alignment: Inspect the valve stem for alignment and smooth operation.\n3. Leak Checks: Examine for leaks in the valve body and connections.\n4. Positioner Calibration: Ensure the valve positioner is calibrated and functioning accurately.\n5. Seal and Packing: Check and replace worn seals and packing to prevent leaks.",
    "hi": "Welcome to the Honeywell Generative AI System! How may I assist you today?",
    
}

@csrf_exempt  # Decorator to exempt the view from CSRF verification
@require_POST  # Ensures that the view only accepts POST requests
def chat(request):
    """
    Process chat messages received via POST requests and return a JSON response.

    Args:
        request (HttpRequest): The Django HttpRequest object containing metadata and user data.

    Returns:
        JsonResponse: Contains the chatbot's response along with the CSRF token.
    """
    data = request.POST  # If you're sending data as form data
    print(f"Received data: {data}")
    user_input = data.get('message', '')
    print(f"Received message: {user_input}")
    
    # Get the CSRF token
    csrf_token = get_token(request)
    
    # Your logic to process the message and generate a response
    data = request.POST
    user_input = data['message']
    print(f"Received message: {user_input}")
    response = get_response(user_input)
    print(f"Sending response: {response}")
    
    # Return the response with the CSRF token
    return JsonResponse({'response': response, 'csrf_token': csrf_token})

def get_response(input_text):
    """
    Generate a response based on the input text by checking the knowledge base or using the generative model.

    Args:
        input_text (str): The user's input text to which the chatbot will respond.

    Returns:
        str: The chatbot's response text.
    """
    input_text_processed = input_text.lower()
    print(f"Processed input text: {input_text_processed}")
    
    # Check if the input text matches any predefined responses in the knowledge base
    for key, value in knowledge_base.items():
        if key in input_text_processed:
            time.sleep(1.5) 
            print(f"Returning base response: {value}")
            return value

    # If no predefined response is found, generate a response using the model
    response = chatbot(input_text, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    if response:
        generated_text = response[0]['generated_text']
        eos_token = "<eos>"
        trimmed_text = generated_text.split(eos_token, 1)[0]
        print(f"Returning generated response: {trimmed_text.strip()}")
        return trimmed_text.strip()
    else:
        print("Sorry, I couldn't generate a response.")
        return "Sorry, I couldn't generate a response."
