
### 3. Caso de Estudio: Mesa Redonda

**Descripción**
La siguiente semana es la conferencia anual de Data Science y asistirán 8 expositores de distintas marcas de software. Las veces pasadas que se ha organizado la conferencia ha habido mucha tensión entre expositores, discusiones y todo tipo de conflictos. Este año, se ha determinado que se utilizará un algoritmo para ubicar a los expositores de manera que se reduzcan los conflictos. Para esto, se digitalizó la información de las conferencias pasadas, se determinó un indicador de conflictos (**IDC**) en función a la frecuencia y gravedad de las discusiones entre expositores, y se recopiló los datos en un archivo **participantes.txt**

**Formato del dataset**

|       | Sentencias                                                                |
| :---: | ------------------------------------------------------------------------- |
| 1     | El IDC de Microsoft aumenta en 95 cuando se sienta junto a IBM.           |
| 2     | El IDC de Microsoft disminuye en 36 cuando se sienta junto a Weka.        |
| 3     | El IDC de Microsoft disminuye en 40 cuando se sienta junto a Teradata.    | 
| 4     | El IDC de Microsoft aumenta en 3 cuando se sienta junto a Python.         |
| 5     | El IDC de Microsoft aumenta en 3 cuando se sienta junto a R.              |
| ...   | ...                                                                       |
| 53    | El IDC de RapidMiner aumenta en 8 cuando se sienta junto a Teradata.      |
| 54    | El IDC de RapidMiner disminuye en 13 cuando se sienta junto a Python.     |
| 55    | El IDC de RapidMiner disminuye en 13 cuando se sienta junto a R.          |
| 56    | El IDC de RapidMiner aumenta en 4 cuando se sienta junto a Scala.         |

**Lectura del archivo _(2 puntos)_**

```python
def preprocess():

    dataset = np.loadtxt("mesa_redonda/input/participantes.txt", dtype=str, delimiter='\n')

    transformed_dataset = []

    for sentence in np.nditer(dataset):
        sentence = str(np.array_str(sentence)).replace('.', '').split(' ')

        company1 = sentence[3]
        multiplier = 1 if sentence[4] == 'aumenta' else -1
        idc = float(sentence[6]) * multiplier
        company2 = sentence[12]

        if not company1 in participants:
            participants.append(company1)
        if not company2 in participants:
            participants.append(company2)

        company1_id = participants.index(company1) + 1
        company2_id = participants.index(company2) + 1

        transformed_dataset.append([company1_id, idc, company2_id])

    return transformed_dataset
```

**Participantes**

```python
    ['Microsoft', 'IBM', 'Weka', 'Teradata', 'Python', 'R', 'Scala', 'RapidMiner']
```

**Datos extraidos**

| Id Participante 1 | Indicador de Conflicto | Id Participante 2 |
| :---------------: | ---------------------: | :---------------: |
| 1                 | 95.0                   | 2                 | 
| 1                 | -36.0                  | 3                 | 
| 1                 | -40.0                  | 4                 | 
| 1                 | 3.0                    | 5                 | 
| 1                 | 3.0                    | 6                 | 
| 1                 | -18.0                  | 7                 |
| ...               | ...                    | ...               |

**Matriz de indicadores de conflicto**

|   | 1     |  2    |   3    |  4     | 5      |6       |7       |8       |
|:-:|------:|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **1** |     0 |   95.0|   -36.0|   -40.0|     3.0|     3.0|   -18.0|   -39.0|
| **2** | -40.0 |      0|    -2.0|   -55.0|    93.0|    94.0|    24.0|   -87.0|
| **3** | -14.0 |  -10.0|       0|     2.0|    -3.0|   -50.0|   -42.0|   -59.0|
| **4** | -36.0 |  -18.0|   -15.0|       0|    18.0|    22.0|    -2.0|   -22.0|
| **5** |  15.0 |   94.0|     3.0|    98.0|       0|    10.0|   -55.0|    44.0|
| **6** |  12.0 |   94.0|    15.0|    63.0|    52.0|       0|   -10.0|    58.0|
| **7** |  44.0 |   75.0|   -17.0|    32.0|   -50.0|   -23.0|       0|    39.0|
| **8** |  43.0 |   44.0|   -41.0|     8.0|   -13.0|   -13.0|     4.0|       0|

**Representante más y menos conflictivo. _(2 puntos)_**

```python
def more_less_conflictive(idc_matrix):
    sum_idc_list = []
    size = len(idc_matrix)

    for i in range(size):
        sum_idc_list.append(0)
        for j in range(size):
            sum_idc_list[i] += idc_matrix[i][j]
        for j in range(size):
            if j != i:
                sum_idc_list[i] += idc_matrix[j][i]

    return dict(
        more_conflictive=[participants[sum_idc_list.index(max(sum_idc_list))], max(sum_idc_list)],
        less_conflictive=[participants[sum_idc_list.index(min(sum_idc_list))], min(sum_idc_list)],
    )
```

**Resultado**

```python
    {'more_conflictive': ['IBM', 401.0], 'less_conflictive': ['Weka', -269.0]}
```

4. Ordenar a los representantes para minimizar conflictos. **(4 puntos)**

```python
def sort_participants(dataset, k):
    permutations = it.permutations(
        range(1, len(participants) + 1), len(participants))
    permutations = [list(permutation) for permutation in permutations]
    sum_idc_list = []

    for seat_order in permutations:
        sum_idc = 0
        for i in range(1, len(seat_order)):
            idc = get_idc(dataset, seat_order[i - 1], seat_order[i])
            sum_idc += idc
        sum_idc_list.append(sum_idc)

    optimal_order = []

    while k > 0:
        min_idc = min(sum_idc_list)
        index = sum_idc_list.index(min_idc)
        optimal_order.append([permutations[index], min_idc])
        sum_idc_list[index] = float('Inf')
        k -= 1

    return optimal_order
```

**10 mejores ordenaciones óptimas de participantes**

|Id|Id|Id|Id|Id|Id|Id|Id|IDC|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|--:|
|1| 4| 2| 8| 3| 6| 7| 5| -296.0| 
|2| 4| 1| 8| 3| 6| 7| 5| -281.0| 
|1| 4| 2| 8| 5| 7| 3| 6| -280.0| 
|2| 4| 1| 3| 8| 5| 7| 6| -277.0| 
|7| 5| 1| 4| 2| 8| 3| 6| -271.0| 
|1| 4| 2| 8| 3| 7| 5| 6| -268.0| 
|1| 4| 2| 8| 3| 5| 7| 6| -267.0| 
|6| 1| 4| 2| 8| 3| 7| 5| -266.0| 
|2| 4| 1| 8| 5| 7| 3| 6| -265.0| 
|2| 8| 3| 6| 7| 5| 1| 4| -263.0|

**Solución**
- Microsoft se debe sentar junto a Teradata debido a que el IDC disminuye en 40.0 cuando estan juntos
- Teradata se debe sentar junto a IBM debido a que el IDC disminuye en 18.0 cuando estan juntos
- IBM se debe sentar junto a RapidMiner debido a que el IDC disminuye en 87.0 cuando estan juntos
- RapidMiner se debe sentar junto a Weka debido a que el IDC disminuye en 41.0 cuando estan juntos
- Weka se debe sentar junto a R debido a que el IDC disminuye en 50.0 cuando estan juntos
- R se debe sentar junto a Scala debido a que el IDC disminuye en 10.0 cuando estan juntos
- Scala se debe sentar junto a Python debido a que el IDC disminuye en 50.0 cuando estan juntos

**Generación de 10 matrices de 8x8 con IDC aleatorios entre -100 y 100, tome en cuenta que el valor fila-columna tiene que ser igual a columna-fila, además que fila=columna es 0. Cada matriz guardar en un archivo tipo csv, con nombre “Dataset”<nro>”.csv” _(2 puntos)_**

```python
def generate_idc_matrix(m=8, n=8, numfiles=10):

    for numfile in range(1, numfiles + 1):

        random_idc_matrix = []

        for i in range(m):
            random_idc_matrix.append([])
            for j in range(n):
                if i == j:
                    random_idc = 0
                else:
                    random_idc = np.random.randint(low=-100, high=100, size=1)[0]

                random_idc_matrix[i].append(random_idc)

        for i in range(m):
            for j in range(n):
                random_idc_matrix[i][j] = random_idc_matrix[j][i]

        df = pd.DataFrame(random_idc_matrix)
        df.to_csv('mesa_redonda/output/Dataset{0}.csv'.format(numfile), index=None, header=False)

```

**Datasets generados**

- [Dataset1.csv](output/Dataset1.csv)
- [Dataset2.csv](output/Dataset2.csv)
- [Dataset3.csv](output/Dataset3.csv)
- [Dataset4.csv](output/Dataset4.csv)
- [Dataset5.csv](output/Dataset5.csv)
- [Dataset6.csv](output/Dataset6.csv)
- [Dataset7.csv](output/Dataset7.csv)
- [Dataset8.csv](output/Dataset8.csv)
- [Dataset9.csv](output/Dataset9.csv)
- [Dataset10.csv](output/Dataset10.csv)