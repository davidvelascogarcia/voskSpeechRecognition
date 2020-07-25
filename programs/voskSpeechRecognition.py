'''
  * ************************************************************
  *      Program: Vosk Speech Recognition Module
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ************************************************************
  *
  * | INPUT PORT                           | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /voskSpeechRecognition/data:i        | Input audio to recognize                                |
  *
  * | OUTPUT PORT                          | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /voskSpeechRecognition/data:o        | Recognized output text                                 |
  *
'''

# Libraries
import configparser
import datetime
import os
import platform
import pyaudio
import sys
import time
from vosk import Model, KaldiRecognizer
import yarp

print("**************************************************************************")
print("**************************************************************************")
print("               Program: Vosk Speech Recognition Module                    ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")
print("")

print("")
print("Loading Vosk Speech Recognition module ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("**************************************************************************")
print("Language configuration:")
print("**************************************************************************")
print("")

# Variable to loopControlFileExists
loopControlFileExists = 0

while int(loopControlFileExists)==0:

    # If file founded
    try:
        # Get language config
        print("")
        print("Getting language configuration ...")
        print("")
        languageConfigurationObject = configparser.ConfigParser()
        languageConfigurationObject.read('../config/language.ini')
        languageConfigurationObject.sections()

        userLanguage = languageConfigurationObject['Language']['user-language']

        print("")
        print("[INFO] User language: " + str(userLanguage))
        print("")

        # Set loopControlFileExists
        loopControlFileExists = 1

    # If file not founded
    except:
        print("")
        print("[ERROR] Sorry, language.ini not founded, waiting 4 seconds to the next check ...")
        print("")
        time.sleep(4)

print("")
print("[INFO] Data obtained correctly.")
print("")

print("")
print("**************************************************************************")
print("Loading language model:")
print("**************************************************************************")
print("")
print("[INFO] Loading "+ str(userLanguage) + " language model ...")
print("")

# Variable to loopControlModelExist
loopControlModelExist = 0

while int(loopControlModelExist) == 0:

    # If model exist
    try:
        # Get full model path
        modelPath = "./../models/model-" + str(userLanguage)

        # Load full model path
        voskSpeechRecognitionModel = Model(modelPath)
        print("")
        print("[INFO] Model loaded correctly.")
        print("")

        # Set loopControlModelExist
        loopControlModelExist = 1

    # If model not located
    except:
        print("")
        print("[ERROR] Model not founded, next check in 4 seconds.")
        print("")
        time.sleep(4)

print("")
print("**************************************************************************")
print("Initializing voskSpeechRecognitionEngine:")
print("**************************************************************************")
print("")
print("[INFO] Initializing voskSpeechRecognitionEngine ...")
print("")

# Variable to loopControlInitEngine
loopControlInitEngine = 0

while int(loopControlInitEngine) == 0:

    try:
        # Init kaldi recognizer
        print("")
        print("Initializing engine ...")
        print("")

        # Build engine
        voskSpeechRecognitionEngine = KaldiRecognizer(voskSpeechRecognitionModel, 16000)

        print("")
        print("[INFO] voskSpeechRecognitionEngine initialized correctly")
        print("")

        # Set loopControlInitEngine
        loopControlInitEngine = 1

    except:
        print("")
        print("[ERROR] Error initializing voskSpeechRecognitionEngine, next try in 4 seconds.")
        print("")
        time.sleep(4)

print("")
print("**************************************************************************")
print("Initializing microphone:")
print("**************************************************************************")
print("")
print("[INFO] Initializing microphone ...")
print("")

# Variable to loopControlInitMicrophone
loopControlInitMicrophone = 0

while int(loopControlInitMicrophone) == 0:

    try:
        print("")
        print("Initializing microphone access ...")
        print("")

        # Build microphone object
        microphoneEngine = pyaudio.PyAudio()

        # Open microphone
        voskSpeechRecognitionMicrophone = microphoneEngine.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)

        # Init streaming
        voskSpeechRecognitionMicrophone.start_stream()

        print("")
        print("[INFO] Microphone initialized correctly")
        print("")

        # Set loopControlInitMicrophone
        loopControlInitMicrophone = 1

    except:
        print("")
        print("[ERROR] Error initializing microphone, next try in 4 seconds.")
        print("")
        time.sleep(4)


print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")
print("")

# Init YARP Network
yarp.Network.init()

print("")
print("[INFO] Opening data input port with name /voskSpeechRecognition/data:i ...")
print("")

# Open input voskSpeechRecognition port
voskSpeechRecognition_inputPort = yarp.Port()
voskSpeechRecognition_inputPortName = '/voskSpeechRecognition/data:i'
voskSpeechRecognition_inputPort.open(voskSpeechRecognition_inputPortName)

# Create voskSpeechRecognition input data bottle
voskSpeechRecognitionInputBottle = yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /voskSpeechRecognition/data:o ...")
print("")

# Open output voskSpeechRecognition port
voskSpeechRecognition_outputPort = yarp.Port()
voskSpeechRecognition_outputPortName = '/voskSpeechRecognition/data:o'
voskSpeechRecognition_outputPort.open(voskSpeechRecognition_outputPortName)

# Create voskSpeechRecognition output data bottle
voskSpeechRecognitionOutputBottle = yarp.Bottle()

print("")
print("**************************************************************************")
print("Waiting for input audio:")
print("**************************************************************************")
print("")
print("[INFO] Waiting for input audio ...")
print("")

# Variable to loopControlAnalyzingAudio
loopControlAnalyzingAudio = 0

while int(loopControlAnalyzingAudio) == 0:

    print("")
    print("**************************************************************************")
    print("Recognizing audio:")
    print("**************************************************************************")
    print("")
    print("[INFO] Listening audio at " + str(datetime.datetime.now()) + " ...")
    print("")

    # Listened audio
    listenedAudio = voskSpeechRecognitionMicrophone.read(4000)

    # If listenedAudio is empty
    if len(listenedAudio) == 0:
        # Do nothing
        break

    # If detect and recognize final results
    if voskSpeechRecognitionEngine.AcceptWaveform(listenedAudio):

        # Print final results
        recognizedResults = voskSpeechRecognitionEngine.Result()

        # Print recognized results
        print("")
        print("[RESULTS] Recognized results:")
        print("Recognized audio at " + str(datetime.datetime.now()) + ".")
        print("")

        # Print recognizedResults
        print(recognizedResults)

        # Prepare recognized text to send
        parsedRecognizedResults = recognizedResults.split('"text" : "')[1].split('"')[0]

        # Send results with yarp voskSpeechRecognition_outputPort port
        voskSpeechRecognitionOutputBottle.clear()
        voskSpeechRecognitionOutputBottle.addString("RECOGNIZED:")
        voskSpeechRecognitionOutputBottle.addString(str(parsedRecognizedResults))
        voskSpeechRecognitionOutputBottle.addString("DATE:")
        voskSpeechRecognitionOutputBottle.addString(str(datetime.datetime.now()))
        voskSpeechRecognition_outputPort.write(voskSpeechRecognitionOutputBottle)

    # If detect and recognize parcial results
    else:

        # Print partial results
        recognizedPartialResults = voskSpeechRecognitionEngine.PartialResult()

        # Print partial results
        print(recognizedPartialResults)

        # Send None results with yarp voskSpeechRecognition_outputPort port
        voskSpeechRecognitionOutputBottle.clear()
        voskSpeechRecognitionOutputBottle.addString("RECOGNIZED:")
        voskSpeechRecognitionOutputBottle.addString("None")
        voskSpeechRecognitionOutputBottle.addString("DATE:")
        voskSpeechRecognitionOutputBottle.addString(str(datetime.datetime.now()))
        voskSpeechRecognition_outputPort.write(voskSpeechRecognitionOutputBottle)

# Close YARP ports
print("[INFO] Closing YARP ports ...")
voskSpeechRecognition_inputPort.close()
voskSpeechRecognition_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("voskSpeechRecognition program finished correctly.")
print("")
