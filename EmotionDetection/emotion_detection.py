import requests 
import json

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header ={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 
    
    if response.status_code == 400:
        return {
            "anger" : None,
            "disgust" : None,
            "fear": None,
            "joy": None, 
            "sadness": None,
            "dominant_emotion" : None
        }
        
    response_dict = json.loads(response.text)
    list_emotions = response_dict["emotionPredictions"][0]['emotion']

    highest_value = 0
    for emotion in list_emotions.keys():
        cur_value = list_emotions[emotion]
        cur_emotion = emotion
        if cur_value > highest_value:
            dominant_emotion = emotion
            highest_value = cur_value
    list_emotions['dominant_emotion'] = dominant_emotion
    return list_emotions



