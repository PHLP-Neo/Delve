import keyboard

print("Press 'w' to trigger an action. Press 'esc' to exit.")


while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'w':
            print("Action for 'w'")
        elif event.name == 'd':
            print("Action for 'd'")
        elif event.name == 'esc':
            print("Exiting...")
            break
