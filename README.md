# Uni Agency Summarize API 
The API that can analyze the text you provide to it works in English

# Technologies
- FastAPI
- Redis
- Docker
- Pydantic


# Instructions
```text
1. git clone https://github.com/AntonShpakovych/uni-agency-summarize.git
2. cd uni-agency-summarize or your name
3. create .env in project root (example provided in env.sample)
4. docker compose up --build
5. Then just wait for application startup (few minutes, lifespan initialize model)
6. After you will see `Application startup complete.` you can go to http://127.0.0.1/docs/
```

# Examples
### Example 1 (Valid)
##### Request: post /summarize
```json
{
    "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
}
```
##### Response:
```json
{
    "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world."
}
```
### Examlple 2 (To many Requests)
##### Request: post /summarize
```json
{
    "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
}
```
And the next request was made immediately
```json

{
    "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
}
```
##### Response
```json
{
  "detail": "Too Many Requests",
  "status_code": 429
}
```
Basic limitations for this endpoint, you can use it once every 30 seconds
### Example 3 (Only English)
##### Request: post /summarize
```json
{
    "text": "Різноманітність природи здатна зачарувати навіть найбільш суворого спостерігача. Величезні гори, що височіють у небо, струмки, що мовчазно розливаються серед зелених лісів, і лани, що вкриті квітами, усе це тільки частка величі природи. Запах свіжої трави, спів птахів і шепіт вітру створюють незабутню атмосферу гармонії та спокою. Прогулянки лісом дарують можливість відчути всю цю красу, доторкнутися до природи, забути про турботи і проблеми. Кожен момент у природі – це подарунок, що варто вдячно приймати і насолоджуватися. Тому не забувайте відчувати її дива, вони дарують нам багато незабутніх митей."
}
```
##### Response
```json
{
  "detail": "Only English is allowed",
  "status_code": 400
}
```
# Documentation
- http://127.0.0.1/docs/
