import time
import RPi.GPIO as GPIO

# Set GPIO pins
TRANSMITTER_PIN = 27
RECEIVER_PIN = 17

# Set pulse durations
PULSE_HIGH_DURATION = 0.006  # High pulse duration in seconds
PULSE_LOW_DURATION = 0.006  # Low pulse duration in seconds

# Set binary data to send
test_str = str((input("What code"))) 
binary_data = ''.join(format(ord(i), '08b') for i in test_str)
def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMITTER_PIN, GPIO.OUT)
    GPIO.setup(RECEIVER_PIN, GPIO.IN)

def send_binary_data(data):
    for bit in data:
        if bit == '1':
            GPIO.output(TRANSMITTER_PIN, GPIO.HIGH)
            time.sleep(PULSE_HIGH_DURATION)
            GPIO.output(TRANSMITTER_PIN, GPIO.LOW)
            time.sleep(PULSE_LOW_DURATION)
        else:
            GPIO.output(TRANSMITTER_PIN, GPIO.LOW)
            time.sleep(PULSE_HIGH_DURATION)
            GPIO.output(TRANSMITTER_PIN, GPIO.LOW)
            time.sleep(PULSE_LOW_DURATION)
        



def receive_binary_data():
    received_data = ""
    while True:
        if GPIO.input(RECEIVER_PIN) == GPIO.HIGH:
            received_data += "1"
            time.sleep(PULSE_LOW_DURATION + PULSE_HIGH_DURATION)

            
        else:
            received_data += "0"
            time.sleep(PULSE_LOW_DURATION + PULSE_HIGH_DURATION)
            
    
        if len(received_data) == 8:
            break
    return received_data
    def decode_binary_string(received_data):
        return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


def cleanup_gpio():
    GPIO.cleanup()

# Main program
if __name__ == "__main__":
    try:
        setup_gpio()

        # Sending data
        print("Sending data:", binary_data)
        send_binary_data(binary_data)

        time.sleep(1) 

        # Receiving data
        received_data = receive_binary_data()
        print("Received data:", received_data)
        Decoded_code = decode_binary_string()
        print(Decoded_code)

    except KeyboardInterrupt:
        pass

    finally:
        cleanup_gpio()
