import asyncio
import edge_tts
import pygame
import os

Bot_name = "zenith"

pygame.mixer.init()

async def speak_async(text):
    filename = "zenith_temp.mp3"

    communicate = edge_tts.Communicate(text, "en-US-ChristopherNeural")
    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(filename)

def speak(text):
    print(f"{Bot_name}: {text}")
    asyncio.run(speak_async(text))