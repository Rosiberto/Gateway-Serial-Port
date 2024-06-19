# ThingSpeak Gateway Serial Port
(by Rosiberto Santos)


**Passo a Passo para usar o Gateway**

#1. Conecte seu arduino ao computador (desktop ou notebook)
 
#2. Dê dois cliques no arquivo ThingSpeak-Gateway.exe 

#3. Digite o número da Porta que o Arduino foi reconhecido e aperte ENTER

#4. Informe o Canal do ThingSpeak para qual deseja enviar os dados e aperte ENTER

#5. Informe a sua Write Api Key para conseguir salvar os dados no canal e pressione ENTER

#6. Pronto!! Agora é só curtir!!!

#7. Para finalizar o Gateway, basta pressionar a letra 'q'

#8. No código do arduino, você deve informar TODOS os FIELDS do ThingSpeak a ser utilizado, incluindo a eles, a leitura do sensor conforme exemplo abaixo:



**Para um sensor**

```
void setup() {
  Serial.begin(9600);  
}

  void loop() {
  
  //faz a leitura de um sensor analógico qualquer 
  leituraSensor = analogRead(porta_sensor);
  
  // escreve o valor lido pelo sensor na serial concatenado ao field1
  // este field1 refere-se ao field1 do ThingSpeak que armazenará o resultado na nuvem
  Serial.println(String("field1:")+leituraSensor);

  // aguarda 15seg para enviar a próxima leitura
  delay(15000);
}
```

<br>

**Para vários sensores**
```
void setup() {
  Serial.begin(9600);  
}

  void loop() {
  
  leituraSensor1 = analogRead(porta_sensor1);
  leituraSensor2 = digitalRead(porta_sensor2);
  leituraSensor3 = analogRead(porta_sensor3);
  
  // escreve o valor lido pelo sensor na serial  
  Serial.println( String("field1:")+leituraSensor1 );  
  
  // aguarda 15seg para enviar a leitura do próximo sensor
  delay(15000);
  
  // os passos se repetem
  Serial.println( String("field2:")+leituraSensor2 );  
  delay(15000);
  
  Serial.println( String("field3:")+leituraSensor3 );  
  delay(15000);
  
  
}
```

<br>
<br>

# ReFLeX.IoT Gateway Serial Port
(by Rosiberto Santos)


**Passo a Passo para usar o Gateway**

1. Conecte seu arduino ao computador (desktop ou notebook)
 
2. Dê dois cliques no arquivo ReFLeX.IoT-Gateway.exe 

3. Digite o número da Porta que o Arduino foi reconhecido e aperte ENTER

4. Informe:
	- *URL Host*, local onde está hospedado o ReFLeX.IoT;
	- Resource;
	- API Key;
	- Device ID.
	
	**Obs:** *Resource, API Key* e *Device ID* devem ser os mesmos cadastrados na UI do ReFLeX.IoT no menu ***Provisioning***.


6. Pronto!! Agora é só curtir!!!

7. Para finalizar o Gateway, basta pressionar a letra 'q'

8. No código do arduino, você deve informar TODOS os *PARÂMETROS* do AgentJSON a ser utilizado de acordo com o sensor, incluindo a eles, a leitura do sensor conforme exemplo abaixo:

<br>

```
void loop() {
  
  // h = armazena a umidade   
  // t = armazena a temperatura 
  h = dht.readHumidity();
  t = dht.readTemperature();
  
  // "t:" e "h:" são os parâmetros que o agentJSON espera receber no ReFLeX.IoT
  Serial.println( String("t:")+t );
  
  // uma pausa entre os envios
  delay(5000); 
  
  Serial.println( String("h:")+h );
  delay(5000);  
  
}
```