# AiC-practica-1

## main.py:

Aquest fitxer, contindrà el programa principal del mètode iteratiu.

En primer lloc, es crea un nou objecte del tipus *ArgumentParser*, que contindrà tota la informació necessària par a analitzar la línia de comandes amb els tipus de dades de Python.

Aquest objecte té diversos paràmetres, però només se'n modificarà un. El paràmetre *description*. Aquest paràmetre dóna una breu descripció del que fa el programa i de com funciona.

Seguidament, realitzem una crida a la funció *add\_argument(),* que defineix com s’ha d’interpretar un determinat argument de la línia de comandes. S’ha realitzar una modificació d’un dels arguments de la funció. L’argument en qüestió, és l’argument *help*, que dóna una breu descripció del que fa l’argument.

El següent pas és convertir les cadenes d’arguments en objectes gràcies a la funció *parse\_args().*

Seguidament, s’obtenen els valors n, h, alpha, beta amb la funció integrada en el script descrit anteriorment.

Finalment, es realitzen els càlculs pertinents i s’escriuen els resultats en un fitxer anomenat: *output.ans*

## mainRecursive.py:

L’estratègia seguida és la mateixa que en l’script main.py de la versió iterativa.  **calculs.py:** 

En aquest script, és on es realitzen els càlculs en format iteratiu.

En  obrir  el  fitxer  de  Python,  el  primer  mètode  que  s’observa  és  un  mètode  anomenat calc\_impossiblepont, el qual retorna veritat o fals segons si l'aqüeducte es possible o no.

Aquest mètode utilitza la següent línia de codi per calcular l’alçada del pont:

height = math.sqrt((r \*\* 2 - ((disX - posantX - r) \*\* 2))) + (h - r) on:

- r = radi
- disX = distància entre pilars
- posantX = primer pilar
- h = alçada total del pont

Un cop calculada l’alçada del pont, es retorna cert o fals en funció de si aquesta altura, recentment calculada, és major a la coordenada ‘y’ del terreny.

El següent és el mètode calc\_impossible, el qual calcula la possibilitat de crear o no l’aqüeducte. Per calcular aquesta possibilitat, en primer lloc es calcula el radi de la semicircunferencia de sota de l’aqüeducte com “d / 2” on ‘d’ és la distància entre pilars. Seguidament es calcula el punt màxim on pot arribar la coordenada y del terreny. Aquest càlcul es realitza com “h - r”, on ‘h’ és l’alçada màxima del pont i ‘r’ és el radi. Es retornarà cert o fals en funció de si aquest últim càlcul és major a la coordenada ‘y’ del terreny o no.

A continuació, s’observa el mètode obtainValues, el qual introdueix en llistes les coordenades ‘x’ del terreny, les coordenades ‘y’ del terreny i les distàncies entre pilars.

Les distàncies entre pilars es calculen com la coordenada ‘x’ del pilar de la dreta menys la coordenada ‘x’ del pilar de l’esquerra. Finalment, es retornen les tres llistes de valors.

El següent, és un mètode que senzillament retorna les coordenades del terreny donada la seva tupla.

Durant la realització del càlcul, es van fent crides al mètode calc\_impossible (descrit anteriorment) i si en algun moment aquest mètode retorna fals, es talla l’execució del bucle. Finalment es retorna el cost i el booleà que indica la possibilitat de la construcció o no de l’aqüeducte.

Com a última funció de càlculs hi ha costPont, la qual calcula el cost de la construcció d’un pont. Per realitzar el càlcul, s’empra la fórmula vista en la descripció del mètode anterior però ara amb el pont.

cost = ((alpha \* costsAltPont) + (beta \* (dPont \*\* 2))) on:

- costsAltPont = (h - alt[0]) + (h - alt[n - 1])
- dPont = disX[n - 1] - dis[0]
- la llista ‘alt’ son les coordenades ‘y’ del terreny.

Si en algún moment la crida a calc\_impossiblepont, descrit anteriorment, retorna fals, es talla l’execució del bucle.

Finalment, es retorna el cost i la variable booleana que indica la possibilitat, o no, de construir el pont.

Finalment, en aquest script es troba la funció *calculate*, la qual, primerament, obté els valors de les coordenades ‘x’ i ‘y’ (per separat) i després les distàncies entre pilars.

Seguidament, és comprova per n == 2 si es possible la construcció de l’aqüeducte i en cas que

*n*≠ 2 s’estableixen els casos del *else*. En primer lloc es calcula tant la possibilitat de construcció com el cost de construcció tant del pont com de l’aqüeducte. Finalment, es comprova segons les impossibilitats i si un cost es major a l’altre quin és el cost que s’ha de retornar.

## calculsRecursive.py:

En aquest script, s’han transformat a recursiu únicament les funcions de càlcul de costs. És a dir, s’han transformat les funcions *costPont()* i *costAque().*
