import os
from PIL import Image

def display_compatible_formats():
    formats = ["JPG" , "JPEG", "PNG", "GIF", "BMP", "TIFF", "WEBP"]
    print ("Available formats:")
    for format in formats:
        print (f"- {format}")
    return formats

def convert_image(image_path, output_format, destination_folder=None):
    try:
        if not os.path.exists(image_path):
            print(f"Error: Image '{image_path}' does not exist.")
            return None

        image = Image.open(image_path)

        # Obtener información del archivo original
        file_name = os.path.basename(image_path)
        base_name = os.path.splitext(file_name)[0]

        # Carpeta de destino
        if destination_folder is None:
            destination_folder = os.path.dirname(image_path)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Limpiar y normalizar el formato de salida
        output_format = output_format.strip().upper()

        # Ruta final del archivo
        destination_path = os.path.join(destination_folder, f"{base_name}.{output_format.lower()}")

        # Guardar la imagen en el nuevo formato
        image.save(destination_path, format=output_format)
        print(f"✅ Image converted and saved in: {destination_path}")

        return destination_path

    except Exception as e:
        print(f"Error when converting the image: {e}")
        return None



def convert_multiple_images(image_path, output_format, destination_folder=None):
    if not os.path.exists(image_path):
        print (f"Error: The folder {image_path} do not exist")
        return 0

    formats = ["jpg" , "jpeg", "png", "gif", "bmp", "tiff", "webp"]

    #Cont for files converted
    cont = 0

    #Iterate through the files in the folder
    for file in os.listdir(image_path):
        file_path = os.path.join(image_path, file)

        if os.path.isfile(file_path) and any(file.lower().endswith(ext) for ext in formats):
            #Converting image
            if convert_image(file_path, output_format, destination_folder):
                cont = cont + 1
            
    return cont

def main():
    print ("===IMAGES CONVERTER ===")

    display_compatible_formats()
    print ("\n")

    print("Options:")
    print("1. Convert a single image")
    print("2. Convert multiple images within a folder")

    option = input("Choose an option (1-2): ")
    if option == "1":
        image_path = input ("Insert the path of the image you want to convert: ")
        output_format = input ("Insert the format you want to convert the image to (ej: PNG): ")
        destination_folder = input ("Insert the destination folder where you want to save the converted image (leave it empty to use the same folder as the original image): ")

        if not destination_folder:
            destination_folder = None

        convert_image(image_path, output_format, destination_folder)
    
    elif option == "2":
        image_path = input ("Insert the path of the image you want to convert: ")
        output_format = input ("Insert the format you want to convert the image to (ej: PNG): ")
        destination_folder = input ("Insert the destination folder where you want to save the converted image (leave it empty to use the same folder as the original image): ")

        if not destination_folder:
            destination_folder = None

        num_images_convert = convert_multiple_images(image_path, output_format, destination_folder)
        print (f"\n It converted {num_images_convert} images successfully!")

    else:
        print ("Invalid option")


if __name__ == "__main__":
    main()