import os
import soundfile as sf

input_folder = "train_audio"
output_folder = 'wav_train_audio'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for folder_name in os.listdir(input_folder):
    for filename in os.listdir(os.path.join(input_folder, folder_name)):
        if filename.endswith('.ogg'):
            input_file_path = os.path.join(input_folder, folder_name, filename)

            data, samplerate = sf.read(input_file_path)

            output_file_path = os.path.join(
                output_folder, folder_name, os.path.splitext(filename)[0] + '.wav')

            if not os.path.exists(os.path.join(
                output_folder, folder_name)):
                os.makedirs(os.path.join(
                output_folder, folder_name))

            sf.write(output_file_path, data, samplerate)

            print(f'Converted {input_file_path} to {output_file_path}')

print('Conversion complete.')
