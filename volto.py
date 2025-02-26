# Modulo di OpenCV, libreria per la visione artificiale e il processing delle immagini
import cv2

# Libreria utilizzata per il rilevamento dei volti
import mediapipe as mp

# Modulo per il rilevamento dei volti
rilevazioneVolti = mp.solutions.face_detection

# Modulo per disegnare sui frame delle immagini
disegnoFrame = mp.solutions.drawing_utils

# Creo un oggetto di rilevamento facciale
# model_selection = 1, è usato per rilevamento facciale su scenari dinamici o a distanze ravvicinate
face_detection = rilevazioneVolti.FaceDetection(model_selection=1, min_detection_confidence=0.5)

# Apro la videocamere
videocamera = cv2.VideoCapture(0)

# Ciclo che legge dal video fino a che la videocamera è attiva
while videocamera.isOpened():

    # successo è un booleano che indica se il frame nel video è stato letto correttamente
    # immaggine, è l'immagine effettivamente letta
    # videocamera.read() serve per leggere il frame successivo dal video
    successo, immagine = videocamera.read()
    if not successo:
        continue

    # Per il rilevamento dei volti ho usato MediaPipe che usa il formato RGB per processare le immagini
    # Converti l'immagine da BGR(usato da OpenCV) a RGB
    immagine = cv2.cvtColor(immagine, cv2.COLOR_BGR2RGB)

    # Analizzo l'immagine per rilevare il volto
    risultato = face_detection.process(immagine)

    # Per visualizzare il risultato converto nuovamente l'immaggine, da RGB a BGR per la visualizzazione con OpenCV
    immagine = cv2.cvtColor(immagine, cv2.COLOR_RGB2BGR)

    # Controllo se ci sono rilevamenti, se ci sono disegno dei punti sul volto rilevato
    if risultato.detections:
        for rilevamento in risultato.detections:
            disegnoFrame.draw_detection(immagine, rilevamento)

    # Mostro il video in una finestra
    cv2.imshow('Rilevamento Volto', immagine)

    # Semplice controllo di chiusare del programma senza fare ctrl + c dal terminale
    # Arresto il ciclo di apertura della fotocamera se viene premuto il tasto esc (ha codice 27)
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Chiudo la fotocamera e la finestra
videocamera.release()
