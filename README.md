# rilevamento-volto
Rilevamento Volti in Tempo Reale con OpenCV e MediaPipe.

Questo progetto implementa un sistema di rilevamento facciale in tempo reale utilizzando OpenCV e MediaPipe. La webcam viene utilizzata per acquisire i fotogrammi, che vengono elaborati per identificare i volti presenti nell'inquadratura. Il rilevamento viene effettuato con MediaPipe Face Detection, una soluzione ottimizzata per il riconoscimento facciale rapido ed efficiente.

Funzionalità
- Rilevamento automatico del volto in tempo reale tramite la webcam.
- Disegno di bounding box attorno ai volti rilevati per evidenziarli.
- Conversione dei colori tra gli spazi BGR e RGB per garantire la compatibilità tra OpenCV e
  MediaPipe.
- Possibilità di chiudere il programma premendo il tasto ESC.

Requisiti
Assicurati di avere installate le seguenti librerie Python prima di eseguire il programma:
pip install opencv-python mediapipe

Avvio del programma
Per avviare il programma, esegui lo script Python:
python volto.py
