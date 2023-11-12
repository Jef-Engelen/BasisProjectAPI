Ik heb code geschreven voor een API waarmee een boodschappenlijst mee gemaakt kan worden.
Er zijn 2 get endpoints, een delete endpoint en een put endpoint aanwezig.
De output wordt verstuurd naar http://127.0.0.1:5000/api/groceries. Ik gebruik poort 5000 omdat ik 
problemen had met de standaardpoort 8000 die uvicorn gebruikt. Er kunnen nog sporen zijn in mijn code
van Flask aangezien ik oorspronkelijk moeilijkheden had met FastAPI en dus Flask als alternatief had
gekozen maar uiteindelijk toch weer FastAPI gebruikt heb. Ik ben er niet in geslaagd om mijn applicatie
te deployen, er waren enkele errors waar ik geen oplossing voor gevonden heb. De dockerfile en
docker-compose file zijn wel aanwezig in mijn project.

In onderstaande links vindt u screenshots van Postman requests met de outputs.
![image](https://github.com/Jef-Engelen/BasisProject/assets/71663709/ddce4905-1f6a-4112-a4b1-c714f3ed63c3)
![image](https://github.com/Jef-Engelen/BasisProject/assets/71663709/1faadf76-4d25-4eee-9d50-da0065e07f91)
![image](https://github.com/Jef-Engelen/BasisProject/assets/71663709/8f2a555d-6b3e-4b99-8281-45c7ec1109fe)
![image](https://github.com/Jef-Engelen/BasisProject/assets/71663709/b196de9c-09a5-4297-b88f-e011d8e1eed0)
