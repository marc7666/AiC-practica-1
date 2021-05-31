# AiC-practica-1

## Link git:

https://github.com/marc7666/AiC-practica-1.git

## Authors
This project have been developed by:
- [Aarón Arenas](https://github.com/aaron-at97)
- [Marc Cervera](https://github.com/marc7666)

## Especificació formal:

### Precondició: 

n (nombre de punts del terreny), h (alçada desitjada de l'aqüeducte), alpha (factor de cost), beta (factor de cost) => nombres enters (primera linia del fitxer d'entrada)
n linies amb dos nombres cadascuna que representen les coordenades de cada punt del sòl. => (x, y) => coordenades cartesianes => nombres enters

### Postcondició: 

Donades totes les coordenades del terreny, és calcula el cost de fabricar un pont i un aqüeducte (per separat) i finalment es fabrica el que sigui més eficient => En cas que es puguin construir totes les columnes sense superar la altura límit.
En cas que hi hagi una columna que no es pugui construir, el programa treurà per pantalla que no és possible construir un aqüeducte. Encara que l'aqüeducte no sigui possible, el pont ancara podría ésser possible de construir.

## read_file.py:

Primera ment s’ha implementat un script anomenat ‘read\_file.py’, el qual llegeix el fitxer línia a línia.

Primerament, es passa cada línia del fitxer per la funció *strip()* per eliminar possibles espais en blanc.

En segon lloc, s’introdueix la totalitat del fitxer a l’interior d’una llista, per així facilitar la feina posterior.

Seguidament, amb l’ajuda de la funció *map()* s’obtenen les variables pertanyents a les dades del problema (variables n, h, aplha, beta). Per obtenir cada valor per separat, s’empra la següent línia de codi:

n, h, alpha, beta = map(int, filtered\_reader[0].split(data\_separation))

La funció map, en aquest cas, converteix a enter la posició 0 del *filtered\_reader*, posició en la qual es troben les variables en qüestió. Gràcies a la funció *split(),*  s’obté  cada valor per separat. *data\_separation* és un paràmetre de la funció de lectura del fitxer que indica el criteri de separació a aplicar en el moment de la crida a la funció *split()*.

Abans de retornar res, amb la mateixa estratègia, s’introdueix en una llista anomenada *values* les tuples (x, y) les quals representen les coordenades del terreny.

Finalment, és retorna la llista *values,* n, h, aplha i beta.

## main.py:

Aquest fitxer, contindrà el programa principal del mètode iteratiu.

En primer lloc, mitjançant un bucle *for* que va des d'1 fins a 21 s'aniràn generant nombres. Si el nombre generat és menor a 10, aquest nombres es concatenarà darrere d'un 0 i posteriorment s'afegirà a un *String*, anomenat *fitx* que contindrà el nom complet de l'arxiu de test.
Seguidament, s'obtindràn els les dades del problema mitjançant la funció que llegeix el fitxer per a posteriorment realitzar els càlculs oportuns.
A continuació, és treurà per pantallael nom del fitxer i el resultat. Per deixar constància, s'obrirà el fitxer *output.ans* per escriure-hi el resultat i posteriorment es tancarà.
Finalment, guardem el contingut del fitxer de test i comprovem el resultat amb el nostre fitxer (el fitxer que ha generat el nostre programa). Si el contingut d'ambdós fitxers és igual, el test és correcte. Aquesta acció és realitza per cadascun dels testos.

## mainRecursive.py:

Aquest script és exactament el mateix que l'anterior, amb la diferència que aquest relitza la crida al fitxer que realitza els càlculs de manera recursiva.

## calculsRecursive.py

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


# Requeriments:

- python main.py <File>
- python mainRecursive.py <File>

Cal destacar que els arxiu *.py* han d’estar en el mateix directori atès que tenen dependències entre ells.
PAGE6

