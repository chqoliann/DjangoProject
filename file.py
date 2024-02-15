"""
import pywifi
import time


def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Получаем первый доступный интерфейс Wi-Fi

    print(f"Scanning for Wi-Fi networks with {iface.name()}...\n")

    iface.scan()  # Начинаем сканирование
    time.sleep(2)  # Подождем некоторое время для получения результатов

    scan_results = iface.scan_results()

    print("Available Wi-Fi networks:")
    for result in scan_results:
        print(f"SSID: {result.ssid}, Signal Strength: {result.signal}")


if __name__ == "__main__":
    scan_wifi()def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Получаем первый доступный интерфейс Wi-Fi

    iface.disconnect()  # Отключаемся от текущей сети (если подключены)
    time.sleep(1)

    profile = pywifi.Profile()
    profile.ssid = ssid  # Имя (SSID) сети, к которой хотим подключиться
    profile.auth = pywifi.const.AUTH_ALG_OPEN  # Тип аутентификации (здесь: открытая)
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # Метод аутентификации WPA2
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # Тип шифрования CCMP (AES)

    profile.key = password  # Пароль для подключения к сети (если не требуется, оставьте пустым)

    iface.remove_all_network_profiles()  # Удаляем все профили сетей
    temp_profile = iface.add_network_profile(profile)  # Добавляем профиль сети
    iface.connect(temp_profile)  # Подключаемся к сети

    time.sleep(2)
    return iface.status() == pywifi.const.IFACE_CONNECTED  # Возвращаем True, если подключение успешно

if __name__ == "__main__":
    ssid = "ACA"
    password = "codeacademy"

    if connect_to_wifi(ssid, password):
        print(f"Successfully connected to {ssid}")
    else:
        print(f"Failed to connect to {ssid}")
"""
