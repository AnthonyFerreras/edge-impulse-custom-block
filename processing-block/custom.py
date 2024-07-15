import numpy as np

def custom_processing(input_data, params, **kwargs):
    # Umbrales para acelerómetro y giroscopio
    threshold_acc = params.get('threshold_acc', 2.0)  # Ajusta este valor según tus necesidades
    threshold_gyro = params.get('threshold_gyro', 500)  # Ajusta este valor según tus necesidades

    def apply_threshold(data, threshold):
        # Aplica el umbral a los datos
        return np.where(np.abs(data) > threshold, data, 0)

    # Procesa cada característica
    for key in input_data.keys():
        if 'acc' in key:
            input_data[key] = apply_threshold(input_data[key], threshold_acc)
        elif 'gyro' in key:
            input_data[key] = apply_threshold(input_data[key], threshold_gyro)

    return input_data

def init():
    return {
        'name': 'Custom Threshold Block',
        'parameters': {
            'threshold_acc': {
                'type': 'float',
                'default': 2.0,
                'description': 'Threshold for accelerometer data'
            },
            'threshold_gyro': {
                'type': 'float',
                'default': 500,
                'description': 'Threshold for gyroscope data'
            }
        }
    }
