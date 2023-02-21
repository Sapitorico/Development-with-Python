<div>
<h1 align="center">Development whit Python3</h1>

<img src="https://user-images.githubusercontent.com/105575956/220216383-93914940-8588-4f2d-8237-3ad2375c47f4.png" width="300" align="left"/> 

# Introduccion

Python es un lenguaje de programación interpretado creado por Guido van Rossum. Está diseñado para ser fácil de leer y escribir, y su sintaxis permite a los programadores expresar conceptos en pocas líneas de código. Python es un lenguaje multiparadigma que admite programación orientada a objetos, programación imperativa y funcional

Python es un lenguaje de programación potente y fácil de aprender. Posee eficientes estructuras de datos de alto nivel y un enfoque sencillo pero eficaz de la programación orientada a objetos. La elegante sintaxis de Python y su tipado dinámico, junto con su naturaleza interpretada, lo convierten en un lenguaje ideal para la creación de scripts y el desarrollo rápido de aplicaciones en muchas áreas y en la mayoría de las plataformas.
El intérprete de Python se amplía fácilmente con nuevas funciones y tipos de datos implementados en C o C++ . Python también es adecuado como lenguaje de extensión para aplicaciones personalizables.

</div>

<details>
<summary><h2>Caracteristicas de python</h2></summary>

* Lenguaje de propocito general: se puede utilizar tanto para escribir una pequeña base de datos personalizada, o una aplicación GUI especializada, o un simple juego.

* Lenguaje de alto nivel: es mas facil entender la lectura y su sintaxis, se escribir programas de forma compacta y legible.

* Es un lenguaje de tipado dinamico: python reconoce el tipo de dato y lo define automaticamente, la variable se adapta segun el tipo de dato que le demos
Ejemplo:
```py
nombre = "Sapitorico" - reconoce que es una string
edad = 21 - reconnoce que el dato es un entero
```

* Lenguaje orientada a objetos: desarrollo con objetos, clases metodos objetos, etc

* Lenguaje interpretaod: interpreta linea por linea y lo transforma a lenguaje maquina, este tiene un interprete que lee las intrucciones, lo que lo hace mas facil manuipular y resolver problemas y cambiar el codigo, lo malo de esto es que lo hace mas lento.

# por que utilizar pytohn?

* cualquier desarrollador puede entender un codigo pytohn, admeas puede ser mas prductrivo ya que reduce las lineas de codigo para realizar tareas, ademas nos ahorramos corchetes y podemos ordenar de mejor manera el codigo, utilizando la indentacion.

* contiene una gran biblioteca estandar de codigo, que son pedazos de codigo reutilizables, que podemos reutilizar para casi cualquier cosa, ademas no carga todas las funcionalidades, sino que carga las que utilizemos para nuestro progrmama, importanto esos poedazos de coigo que nos permite realizar la tarea.

* podemos mezclarlo con otros lenguajes de prormacion

* multiparadigma: podemos trasladar un progrmama echo en pytohn a cualquier otro sistema operatvo

<img src="https://user-images.githubusercontent.com/105575956/220435134-58d905f1-0c2c-4d31-86c5-86d38cd72198.jpg" width="500"/>

</details>

<details>
<summary><h2>Interprete</h2></summary>

<img width="428" align="left" alt="Screenshot 2023-02-21 155701" src="https://user-images.githubusercontent.com/105575956/220434700-7e812603-527c-4b66-88ab-07114749c062.png">


Las funciones de edición de línea del intérprete incluyen edición interactiva, sustitución del historial y completado de código en sistemas que soporten la biblioteca GNU Readline.

Since Python statements often contain spaces or other command in its entirety. Some Python modules are also useful as scripts. These can be invoked using python -m module ..., which executes the source file for module as if you had spelled out its full name on the command line. When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards.

Esto puede hacerse pasando -i antes del script. Cuando el intérprete conoce el nombre del script y la variable de argumentos adicionales en el módulo sys. -m, sys.argv se establece con el nombre completo del módulo localizado. Cuando los comandos se leen desde un tty, se dice que el intérprete está en modo interactivo.

En este modo solicita el siguiente comando con el prompt primario, con el prompt secundario, por defecto tres puntos . El intérprete $ python3. Python 3.

</details>

<details>
<summary><h2>if/else, loops, funciones</h2></summary>

Quizás el tipo de sentencia más conocido sea la sentencia if.

La palabra clave 'elif' es la abreviatura de 'else if', y es útil para evitar una indentación excesiva. Si está comparando el mismo valor con varias constantes, o comprobando tipos o atributos específicos, también puede encontrar útil la sentencia match

La sentencia for en Python difiere un poco de lo que puede estar acostumbrado en C o Pascal.

La sentencia pass no hace nada. Puede ser usada cuando una sentencia es requerida sintácticamente pero el programa no requiere ninguna acción pass # Ocupar-esperar la interrupción del teclado del valor en variables.

Si está utilizando clases para estructurar sus datos

Puede utilizar parámetros posicionales con algunas clases incorporadas que proporcionan un orden para sus atributos . Sólo los nombres independientes son asignados por una sentencia match.

<img src="https://user-images.githubusercontent.com/105575956/220440537-4dc93b0e-e712-40e5-a946-f08beaeb2e28.png" width="400"/>

</details>

<details>
<summary><h2>import & modules</h2></summary>

Un módulo es un fichero que contiene definiciones y sentencias de Python. El nombre del fichero es el nombre del módulo con el sufijo .
Existe incluso una variante para importar todos los nombres que define un módulo

En la mayoría de los casos los programadores de Python no utilizan esta facilidad ya que introduce que ya ha definido. Tenga en cuenta que en general la práctica de importar * de un módulo o paquete está mal vista, ya que a menudo causa código poco legible. Si el nombre del módulo va seguido de as, entonces el nombre que sigue a as se vincula directamente al módulo importado.
También se puede utilizar cuando se utiliza from con efectos similares

__init__. The __init__. Py files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, on the module search path.

<img align="left" src="https://user-images.githubusercontent.com/105575956/220442375-a5094c5a-cd51-40cf-9c9a-37af4abdaf3b.jpg" width="400"/>

En Python, un módulo es un archivo que contiene código Python que puede ser utilizado en otros programas. La importación de módulos te permite acceder a funciones, clases y variables definidas en otros archivos, lo que te permite reutilizar el código y ahorrar tiempo y esfuerzo en el desarrollo de programas.

</details>

<details>
<summary><h2>Data Structures: Lists, Tuples</h2></summary>

En Python, existen varias estructuras de datos predefinidas que te permiten almacenar y manipular datos de manera eficiente. A continuación, te presento un resumen de las principales estructuras de datos en Python 3:

# listas

Una lista es una colección ordenada y mutable de elementos, que se define utilizando corchetes ([]). Los elementos de la lista pueden ser de cualquier tipo, y se pueden agregar, eliminar o modificar en cualquier momento.

```py
mi_lista = [1, 2, 3, "cuatro", "cinco"]
mi_lista.append(6)
mi_lista.remove("cuatro")
print(mi_lista)
```

# Tuplas

Una tupla es una colección ordenada e inmutable de elementos, que se define utilizando paréntesis (()). Los elementos de la tupla pueden ser de cualquier tipo, y no se pueden agregar, eliminar o modificar una vez creada.

```py
mi_tupla = (1, 2, 3, "cuatro", "cinco")
print(mi_tupla[0])
```

# Conjuntos

Un conjunto es una colección no ordenada y mutable de elementos únicos, que se define utilizando llaves ({}). Los elementos del conjunto pueden ser de cualquier tipo, y se pueden agregar o eliminar en cualquier momento.

```py
mi_conjunto = {1, 2, 3, "cuatro", "cinco"}
mi_conjunto.add(6)
mi_conjunto.remove("cuatro")
print(mi_conjunto)
```

# Diccionarios

Un diccionario es una colección no ordenada y mutable de pares clave-valor, que se define utilizando llaves ({}). Las claves deben ser únicas y pueden ser de cualquier tipo inmutable, mientras que los valores pueden ser de cualquier tipo.

```py
mi_diccionario = {"uno": 1, "dos": 2, "tres": 3, "cuatro": "cuatro", "cinco": "cinco"}
mi_diccionario["seis"] = 6
del mi_diccionario["cuatro"]
print(mi_diccionario)
```
    
<img src="https://user-images.githubusercontent.com/105575956/220453704-bd9d73e0-90d8-4b4c-9b66-c08333f7fb8d.png" width="400"/>


</details>



<details>
<summary><h2>Exceptions</h2></summary>

En Python, las excepciones son errores que se producen durante la ejecución de un programa. Cuando se produce una excepción, el programa se detiene y muestra un mensaje de error que indica la causa del problema.

Para manejar las excepciones en Python, se utiliza la estructura de control try-except. El código que puede producir una excepción se coloca dentro del bloque try, y el código que maneja la excepción se coloca dentro del bloque except. Si se produce una excepción dentro del bloque try, el programa salta automáticamente al bloque except, donde se maneja la excepción.

Aquí hay un ejemplo de cómo se utiliza la estructura try-except para manejar una excepción en Python:

```py
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")
```

En este ejemplo, el código intenta dividir 10 por cero, lo que produce una excepción ZeroDivisionError. El programa detecta esta excepción y muestra un mensaje de error adecuado en el bloque except.

Además de la excepción ZeroDivisionError, Python tiene muchas otras excepciones integradas que se pueden utilizar para manejar diferentes tipos de errores. También es posible crear tus propias excepciones personalizadas mediante la definición de una clase de excepción.

En resumen, las excepciones son una parte importante del manejo de errores en Python. Al utilizar la estructura de control try-except, puedes manejar las excepciones de manera efectiva y evitar que tu programa se detenga debido a un error.

```py
# Manejo de excepciones de índice fuera de rango
lista = [1, 2, 3]
try:
    print(lista[3])
except IndexError:
    print("Error: índice fuera de rango")

# Manejo de excepciones de valor incorrecto
numero = input("Ingrese un número: ")
try:
    numero = int(numero)
except ValueError:
    print("Error: el valor ingresado no es un número")

# Manejo de excepciones personalizadas
class ErrorPersonalizado(Exception):
    pass

try:
    raise ErrorPersonalizado("Este es un error personalizado")
except ErrorPersonalizado as e:
    print("Se produjo un error personalizado:", e)
```

En el primer ejemplo, se intenta acceder a un elemento de una lista que no existe, lo que produce una excepción IndexError. En el bloque except, se maneja la excepción y se muestra un mensaje de error adecuado.

En el segundo ejemplo, se pide al usuario que ingrese un número, pero si el valor ingresado no se puede convertir a un entero, se produce una excepción ValueError. El bloque except maneja la excepción y muestra un mensaje de error adecuado.

En el tercer ejemplo, se define una excepción personalizada mediante la definición de una clase de excepción. En el bloque try, se levanta la excepción personalizada, y en el bloque except, se maneja la excepción y se muestra un mensaje de error personalizado.

En Python, también es posible utilizar la cláusula finally para ejecutar código que debe ejecutarse independientemente de si se produce una excepción o no. Aquí hay un ejemplo:

```py
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    print(contenido)
except IOError:
    print("Error: no se pudo leer el archivo")
finally:
    archivo.close()
```

En este ejemplo, el código intenta abrir un archivo y leer su contenido. Si se produce una excepción IOError, se maneja la excepción y se muestra un mensaje de error adecuado. En cualquier caso, el archivo se cierra en el bloque finally.

En resumen, las excepciones son una herramienta poderosa en Python para manejar errores y evitar que el programa se detenga debido a un problema. Al utilizar la estructura de control try-except-finally, puedes manejar las excepciones de manera efectiva y garantizar que tu código se ejecute de manera segura.

En programación, los errores son inevitables, y es importante saber cómo manejarlos de manera efectiva para evitar que el programa se detenga debido a un problema. En Python, los errores se manejan mediante el uso de excepciones, que son objetos que representan un problema que se ha producido durante la ejecución del programa.

Para manejar los errores en Python, se utiliza la estructura de control try-except. El código que puede producir una excepción se coloca dentro del bloque try, y el código que maneja la excepción se coloca dentro del bloque except. Si se produce una excepción dentro del bloque try, el programa salta automáticamente al bloque except, donde se maneja la excepción.

En Python, hay muchos tipos de excepciones integradas que se pueden utilizar para manejar diferentes tipos de errores, como la excepción ZeroDivisionError que se produce cuando se intenta dividir por cero, la excepción IndexError que se produce cuando se intenta acceder a un índice fuera de rango en una lista, y la excepción ValueError que se produce cuando se intenta convertir un valor que no es válido a un tipo de datos determinado.

Además de las excepciones integradas, también es posible definir tus propias excepciones personalizadas mediante la definición de una clase de excepción.

En resumen, los errores son una parte inevitable de la programación, pero con el manejo adecuado de excepciones, puedes evitar que los errores detengan tu programa y garantizar que tu código se ejecute de manera segura. La estructura try-except es una herramienta esencial para manejar excepciones en Python, y al conocer las excepciones integradas y cómo definir tus propias excepciones personalizadas, puedes manejar una amplia variedad de errores de manera efectiva.

</details>

<details>
<summary><h2>Classes and Objects</h2></summary>

En Python, una clase es un conjunto de atributos y métodos que definen un objeto. Un objeto es una instancia de una clase, que puede contener datos y tener la capacidad de realizar acciones específicas.

Para definir una clase, se utiliza la palabra clave class, seguida del nombre de la clase y dos puntos. Luego, se definen los atributos y métodos de la clase. Aquí hay un ejemplo de cómo definir una clase simple:

```py
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
```

En este ejemplo, la clase Persona tiene dos atributos: nombre y edad, y un método llamado saludar(), que imprime un mensaje de saludo en la consola.

Para crear un objeto a partir de una clase, se utiliza la sintaxis NombreDeLaClase() y se pueden proporcionar argumentos para los atributos de la clase. Aquí hay un ejemplo:

```py
persona1 = Persona("Juan", 30)
persona1.saludar()
```

En este ejemplo, se crea un objeto llamado persona1 a partir de la clase Persona y se le asignan los valores "Juan" y 30 a los atributos nombre y edad. Luego, se llama al método saludar() del objeto persona1, que imprime el mensaje "Hola, mi nombre es Juan y tengo 30 años." en la consola.

En Python, los objetos pueden heredar atributos y métodos de otras clases. Esto se logra mediante la definición de una clase hija que hereda de una clase padre. Aquí hay un ejemplo:

```py
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y mi salario es de {self.salario} dólares.")
```

En este ejemplo, la clase Empleado hereda de la clase Persona y tiene un atributo adicional llamado salario y un método llamado presentarse(), que imprime un mensaje de presentación en la consola.

En resumen, las clases y los objetos son fundamentales en la programación orientada a objetos de Python. Las clases definen los atributos y métodos de los objetos, y los objetos son instancias de una clase que contienen datos y tienen la capacidad de realizar acciones específicas. La herencia de clases permite la creación de clases hijas que heredan atributos y métodos de una clase padre. Al comprender cómo definir y utilizar clases y objetos en Python, puedes crear programas más estructurados, fáciles de mantener y extensibles.

Variables that belong to an object or class are referred to as fields. Such functions are called methods of the class. This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.

Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.

The self

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self. When you call a method of this object as myobject. Method, this is automatically converted by Python into MyClass.

Method -this is all the special self is about. This also means that if you have a method which takes no arguments, then you still have to have one argument - the self.

<details>
<summary><h2>Properties, Getters and Setters</h2></summary>

En Python, las propiedades, getters y setters son herramientas que se utilizan para controlar el acceso y la modificación de atributos de una clase. Estas herramientas permiten que los atributos de una clase sean manipulados de forma controlada y segura.

Las propiedades son métodos que se utilizan para acceder y modificar los atributos de una clase. Se definen mediante el uso del decorador @property y se acceden mediante la sintaxis de un atributo. Aquí hay un ejemplo:

```py
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
```

En este ejemplo, la clase Persona tiene un atributo _nombre que se accede a través de la propiedad nombre. La propiedad nombre tiene un getter que devuelve el valor del atributo _nombre y un setter que permite modificar el valor del atributo _nombre. La sintaxis para acceder y modificar la propiedad nombre es similar a la de un atributo normal:

```py
persona = Persona("Juan")
print(persona.nombre)  # Salida: Juan
persona.nombre = "Pedro"
print(persona.nombre)  # Salida: Pedro
```

En este ejemplo, se crea un objeto persona de la clase Persona con el nombre "Juan". Luego, se accede al valor del atributo _nombre a través de la propiedad nombre y se modifica el valor del atributo _nombre a "Pedro" a través del setter de la propiedad nombre.

Los getters y setters son métodos que se utilizan para acceder y modificar los atributos de una clase, respectivamente. Estos métodos se definen de manera similar a las propiedades, pero se llaman explícitamente en lugar de accederse mediante la sintaxis de un atributo. Aquí hay un ejemplo:

```py
class Rectangulo:
    def __init__(self, ancho, altura):
        self._ancho = ancho
        self._altura = altura

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura

    def area(self):
        return self._ancho * self._altura

```

En este ejemplo, la clase Rectangulo tiene dos atributos, _ancho y _altura, que se acceden y modifican mediante los métodos get_ancho(), set_ancho(), get_altura() y set_altura(). El método area() calcula y devuelve el área del rectángulo. Para acceder y modificar los atributos _ancho y _altura, se utilizan los métodos correspondientes:

```py
rectangulo = Rectangulo(10, 20)
print(rectangulo.get_ancho())  # Salida: 10
print(rectangulo.get_altura())  # Salida: 20
rectangulo.set_ancho(5)
rectangulo.set_altura(10)
print(rectangulo.area())  # Salida: 50
```
En este ejemplo, se crea un objeto rectangulo de la clase Rectangulo con un ancho de 10 y una altura de 20.
</details>


</details>


<details>
<summary><h2>Test-driven development</h2></summary>


# Doctests

Los doctest son una herramienta de Python que permiten escribir pruebas en la misma documentación de una función o módulo. Los doctest son útiles porque pueden ayudar a garantizar que el código funciona correctamente al mismo tiempo que proporciona una documentación clara y concisa.

Un ejemplo de doctest podría ser la siguiente función que calcula la suma de dos números:

```py
def suma(a, b):
    """
    Esta función calcula la suma de dos números.

    Ejemplos:
    >>> suma(2, 3)
    5
    >>> suma(-1, 1)
    0
    >>> suma(0, 0)
    0
    """
    return a + b
```
En este ejemplo, la documentación de la función suma incluye ejemplos de cómo se puede llamar la función y qué resultado se espera en cada caso. Los ejemplos están escritos en un formato similar al de una sesión interactiva de Python, donde el símbolo >>> indica una entrada de usuario y el resultado esperado se escribe después.

Para ejecutar los doctest, se utiliza el módulo doctest de Python. Por ejemplo:

```py
import doctest

doctest.testmod()
```

o de forma manual en la temrinal

```py
python3 -m doctest -v
```

Esto ejecuta todos los doctest en un módulo y produce una salida que indica si los resultados esperados coinciden con los resultados reales.

Los doctest son útiles porque permiten asegurarse de que la documentación es precisa y que el código funciona como se espera. Además, los doctest son fáciles de escribir y pueden proporcionar una forma rápida y sencilla de probar pequeñas piezas de código.

Es importante tener en cuenta que los doctest no deben ser utilizados como una herramienta exhaustiva de pruebas. Los doctest sólo prueban los casos de prueba explícitamente incluidos en la documentación, por lo que es necesario utilizar otras herramientas de pruebas para garantizar que el código funciona correctamente en todos los casos posibles.


# Unitests

Unittest es un módulo de Python que se utiliza para escribir y ejecutar pruebas unitarias. Las pruebas unitarias son un tipo de prueba de software que se centra en probar cada componente individual del código para asegurarse de que funciona correctamente.

Para utilizar el módulo Unittest, se crean clases que heredan de unittest.TestCase. Dentro de estas clases, se definen métodos de prueba que utilizan los métodos de aserción proporcionados por Unittest para verificar si el comportamiento del código es el esperado.

Un ejemplo de prueba unitaria con Unittest sería el siguiente:

```py
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

En este ejemplo, se define una función suma que calcula la suma de dos números. Luego, se crea una clase TestSuma que hereda de unittest.TestCase y se definen tres métodos de prueba: test_suma_positivos, test_suma_negativos y test_suma_cero. Cada método de prueba utiliza un método de aserción de Unittest (self.assertEqual) para verificar si el resultado de la función suma coincide con el resultado esperado.

Finalmente, se utiliza la sentencia if __name__ == '__main__' para indicar que se debe ejecutar la función unittest.main() para ejecutar las pruebas.

Unittest es una herramienta poderosa y flexible para escribir pruebas unitarias en Python. Permite definir conjuntos de pruebas complejas y ejecutarlas de forma automatizada. Además, Unittest se integra bien con otras herramientas de pruebas y puede utilizarse en conjunción con doctest para proporcionar una cobertura completa de las pruebas en un proyecto.

El Desarrollo Guiado por Pruebas (Test-driven development, TDD) es una práctica de programación en la que se escriben pruebas antes de escribir el código. El objetivo es mejorar la calidad del código y asegurarse de que cumple con los requisitos específicos.

El proceso de TDD se realiza en tres fases:

Red: escribir una prueba fallida que describa el comportamiento deseado.
Green: escribir el código mínimo necesario para que la prueba pase.
Refactor: mejorar el código existente sin cambiar su comportamiento, asegurándose de que todas las pruebas sigan pasando.
Un ejemplo de TDD podría ser la implementación de una función que sume dos números:

```py
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(-1, 1), 0)
        
def sum(a, b):
    return a + b
```

En este ejemplo, se crea una clase de prueba TestSum que hereda de la clase unittest.TestCase. La clase de prueba tiene un método de prueba test_sum que prueba la función sum con diferentes entradas y compara el resultado con un valor esperado utilizando el método assertEqual. En este caso, la función sum simplemente devuelve la suma de los dos números de entrada.

En la fase "Red" de TDD, la prueba falla porque la función sum no ha sido implementada todavía.

En la fase "Green", se implementa la función sum para que pase las pruebas escritas previamente.

Finalmente, en la fase "Refactor", se puede mejorar el código existente sin cambiar su comportamiento. En este ejemplo, la función sum es bastante simple y no hay mucho que refactorizar, pero en proyectos más grandes, esta fase puede ser muy importante para mantener un código limpio y fácil de entender.

El TDD puede llevar más tiempo al principio, pero a largo plazo puede ahorrar tiempo y dinero, ya que se asegura de que el código funciona como se espera y es fácil de mantener. Además, la práctica del TDD fomenta la escritura de código modular y bien estructurado.

</details>

<details>
<summary><h2>Inheritance</h2></summary>

La herencia es un mecanismo en Python que permite crear nuevas clases basadas en clases ya existentes. La clase existente se llama clase base o clase padre y la nueva clase se llama clase derivada o clase hija. La clase derivada hereda todos los atributos y métodos de la clase padre y puede agregar nuevos atributos y métodos o modificar los ya existentes.

Un ejemplo de herencia en Python es el siguiente:

```py
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def talk(self):
        return "Woof"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        return "Meow"
```

En este ejemplo, se define una clase Animal que tiene dos atributos (name y age) y un método talk que no hace nada. Luego, se definen dos clases derivadas (Dog y Cat) que heredan de la clase Animal.

La clase Dog tiene un atributo adicional (breed) y un método talk que devuelve "Woof". La clase Cat tiene un atributo adicional (color) y un método talk que devuelve "Meow". Ambas clases utilizan el método super() para llamar al constructor de la clase padre y heredar los atributos name y age.

Al utilizar la herencia, se evita tener que repetir el código de la clase base en las clases derivadas. En lugar de eso, se define una vez en la clase base y se reutiliza en las clases derivadas. Además, las clases derivadas pueden agregar comportamiento adicional o modificar el comportamiento existente de la clase base.

En resumen, la herencia es una característica importante de la programación orientada a objetos que permite la reutilización de código y la creación de nuevas clases basadas en clases existentes.

La herencia es una característica importante de la programación orientada a objetos que permite la creación de nuevas clases basadas en clases existentes. La nueva clase, llamada clase derivada o clase hija, hereda todos los atributos y métodos de la clase existente, llamada clase base o clase padre. La herencia facilita la reutilización del código y la organización de las clases en jerarquías.

En Python, la herencia se define utilizando la sintaxis class DerivedClass(BaseClass):. La clase derivada puede agregar nuevos atributos y métodos o modificar los ya existentes. Si la clase derivada define un método con el mismo nombre que uno en la clase base, el método de la clase derivada reemplaza al de la clase base. Sin embargo, la clase derivada puede llamar al método de la clase base utilizando la función super().

Veamos un ejemplo más detallado:

```py
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
```

En este ejemplo, se define una clase base llamada Shape que tiene dos atributos x e y y un método area que no hace nada. Luego, se definen dos clases derivadas: Rectangle y Circle. La clase Rectangle tiene dos atributos adicionales (width y height) y un método area que calcula el área del rectángulo. La clase Circle tiene un atributo adicional (radius) y un método area que calcula el área del círculo.

La clase Rectangle y la clase Circle heredan los atributos y métodos de la clase Shape. Por lo tanto, pueden acceder a los atributos x e y y llamar al método area sin tener que definirlos nuevamente. Además, las clases derivadas agregan atributos y métodos adicionales que son específicos de cada forma.

En resumen, la herencia es una técnica importante de la programación orientada a objetos que permite la reutilización de código y la organización de las clases en jerarquías. En Python, se define utilizando la sintaxis class DerivedClass(BaseClass):. Las clases derivadas heredan todos los atributos y métodos de la clase base y pueden agregar nuevos atributos y métodos o modificar los ya existentes.

</details>

<details>
<summary><h2>Input/Output</h2></summary>

En Python, la entrada y salida (Input/Output, I/O) se manejan utilizando funciones integradas que permiten la lectura y escritura de datos desde y hacia archivos, la consola y otros dispositivos.

La función print() se utiliza para imprimir datos en la consola. Por defecto, la función print() separa los elementos con un espacio y agrega un salto de línea al final. Sin embargo, es posible cambiar estos comportamientos utilizando los argumentos opcionales sep y end. Por ejemplo:

```py
nombre = "Juan"
edad = 25
print("Hola,", nombre, "tienes", edad, "años.")
# Salida: Hola, Juan tienes 25 años.

print("Hola,", nombre, "tienes", edad, "años.", sep="-", end="!\n")
# Salida: Hola-Juan-tienes-25-años.!
```

Para leer datos desde la consola, se utiliza la función input(). Esta función espera que el usuario ingrese una cadena de caracteres y devuelve la cadena como resultado. Por ejemplo:

```py
nombre = input("Ingresa tu nombre: ")
print("Hola,", nombre)
```

Para leer y escribir datos desde y hacia archivos, se utilizan las funciones open(), read() y write(). La función open() se utiliza para abrir un archivo y devuelve un objeto archivo. La función read() se utiliza para leer los datos del archivo y la función write() se utiliza para escribir datos en el archivo. Es importante cerrar el archivo después de usarlo utilizando la función close().

Por ejemplo, para leer los contenidos de un archivo llamado "archivo.txt" y imprimirlos en la consola, se podría hacer lo siguiente:

```py
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

En resumen, en Python, la entrada y salida (Input/Output, I/O) se manejan utilizando funciones integradas que permiten la lectura y escritura de datos desde y hacia archivos, la consola y otros dispositivos. La función print() se utiliza para imprimir datos en la consola, la función input() se utiliza para leer datos desde la consola y las funciones open(), read() y write() se utilizan para leer y escribir datos desde y hacia archivos.
</details>

<details>
<summary>><h2>Python - Almost a circle</h2></summary>


# *args and **kwargs in python explained

En Python, "args" y "kwargs" son dos parámetros especiales que se pueden utilizar en las definiciones de las funciones para recibir argumentos variables.

"Args" es un parámetro que permite a una función recibir un número variable de argumentos no nombrados. Esto significa que se puede pasar cualquier cantidad de argumentos a la función y Python los empacará todos en una tupla. Veamos un ejemplo:

```py
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```

En este ejemplo, definimos una función llamada my_function con un parámetro *args. Luego llamamos a la función con tres argumentos: 1, 2 y 3. Al imprimir los valores de args en el cuerpo de la función, obtenemos:

```py
1
2
3
```

Esto significa que Python empacó los argumentos en una tupla y los pasó a la función.

"Kwargs" es un parámetro que permite a una función recibir un número variable de argumentos nombrados. Esto significa que se puede pasar cualquier cantidad de argumentos con un nombre específico a la función y Python los empacará en un diccionario. Veamos un ejemplo:

```py
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name='Alice', age=30, city='New York')
```

En este ejemplo, definimos una función llamada my_function con un parámetro **kwargs. Luego llamamos a la función con tres argumentos nombrados: name, age y city. Al imprimir los valores de kwargs en el cuerpo de la función, obtenemos:

```py
name Alice
age 30
city New York
```

Esto significa que Python empacó los argumentos nombrados en un diccionario y los pasó a la función.

"Args" y "kwargs" también se pueden combinar en una misma función. En este caso, "args" se utiliza para recibir argumentos no nombrados y "kwargs" se utiliza para recibir argumentos nombrados. Veamos un ejemplo:

```py
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

my_function(1, 2, 3, name='Alice', age=30, city='New York')
```

En este ejemplo, definimos una función llamada my_function con los parámetros *args y **kwargs. Luego llamamos a la función con tres argumentos no nombrados y tres argumentos nombrados. Al imprimir los valores de args y kwargs en el cuerpo de la función, obtenemos:

```py
1
2
3
name Alice
age 30
city New York
```

Esto significa que Python empacó los argumentos no nombrados en una tupla y los argumentos nombrados en un diccionario, y los pasó a la función.

En resumen, "args" y "kwargs" son parámetros especiales que permiten a las funciones de Python recibir argumentos variables. "Args" se utiliza para recibir argumentos no nombrados, mientras que "kwargs" se utiliza para recibir argumentos nombrados. Estos parámetros pueden ayudar a hacer que las funciones sean más flexibles y fáciles de usar.


# JSON encoder and decoder

La librería "json" de Python permite codificar y decodificar datos en formato JSON. JSON es un formato de datos ligero y fácil de leer que se utiliza comúnmente en aplicaciones web y móviles para enviar y recibir datos.

Para usar la librería "json" en Python, primero debemos importarla:

```py
import json
```

Una vez que hemos importado la librería, podemos usar sus funciones para codificar y decodificar datos en formato JSON. Por ejemplo, para codificar un diccionario Python en formato JSON, podemos usar la función json.dumps():

```py
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_str = json.dumps(my_dict)
print(json_str)
```

En este ejemplo, creamos un diccionario llamado my_dict y luego lo codificamos en formato JSON utilizando la función json.dumps(). Luego imprimimos la cadena JSON resultante en la consola.

Para decodificar una cadena JSON en un objeto Python, podemos usar la función json.loads():

```py
json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
my_dict = json.loads(json_str)
print(my_dict)
```

En este ejemplo, creamos una cadena JSON llamada json_str y luego la decodificamos en un diccionario Python utilizando la función json.loads(). Luego imprimimos el diccionario resultante en la consola.

La librería "json" también proporciona opciones avanzadas para personalizar el proceso de codificación y decodificación. Por ejemplo, podemos proporcionar una función personalizada para codificar un objeto en formato JSON utilizando el parámetro default de la función json.dumps():

```py
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def encode_person(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age, 'city': obj.city}
    else:
        raise TypeError('Object of type Person is not JSON serializable')

my_person = Person('Alice', 30, 'New York')
json_str = json.dumps(my_person, default=encode_person)
print(json_str)
```

En este ejemplo, definimos una clase Person que representa una persona con un nombre, una edad y una ciudad. Luego definimos una función encode_person() que se utiliza para codificar objetos de la clase Person en formato JSON. Finalmente, creamos un objeto my_person de la clase Person y lo codificamos en formato JSON utilizando la función json.dumps() y el parámetro default.

En resumen, la librería "json" de Python permite codificar y decodificar datos en formato JSON. Esto es útil para enviar y recibir datos en aplicaciones web y móviles. La librería proporciona funciones simples para codificar y decodificar datos, así como opciones avanzadas para personalizar el proceso de codificación y decodificación.

# Unitests

La biblioteca unittest de Python es un marco de prueba integrado que se utiliza para escribir y ejecutar pruebas unitarias en Python. unittest proporciona una serie de clases y métodos para crear y ejecutar pruebas unitarias.

Para utilizar la biblioteca unittest, primero debemos importarla:

```py
import unittest
```

Luego, podemos crear una clase de prueba que herede de unittest.TestCase. Dentro de esta clase, podemos definir diferentes métodos que contienen las pruebas unitarias que queremos ejecutar. Por ejemplo, el siguiente código define una clase de prueba simple con una prueba unitaria:

```py
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 3)
```

En este ejemplo, creamos una clase llamada MyTestCase que hereda de unittest.TestCase. Luego definimos un método llamado test_addition() que realiza una prueba unitaria simple de suma. La prueba compara el resultado de 1 + 2 con el valor esperado de 3 utilizando el método assertEqual() de unittest.TestCase.

Para ejecutar nuestras pruebas unitarias, podemos usar el método unittest.main(). Por ejemplo, podemos agregar el siguiente código al final de nuestro archivo de prueba para ejecutar todas las pruebas unitarias definidas en nuestra clase de prueba:

```py
if __name__ == '__main__':
    unittest.main()
```

La biblioteca unittest proporciona una amplia variedad de métodos de aserción que se utilizan para verificar el comportamiento esperado de nuestro código en las pruebas unitarias. Algunos de los métodos de aserción más comunes incluyen:

assertEqual(a, b): verifica si a y b son iguales
assertNotEqual(a, b): verifica si a y b no son iguales
assertTrue(x): verifica si x es verdadero
assertFalse(x): verifica si x es falso
assertIn(a, b): verifica si a está en b
assertNotIn(a, b): verifica si a no está en b
assertRaises(exception, callable, *args, **kwds): verifica si callable(*args, **kwds) genera una excepción del tipo exception
A continuación, se muestra un ejemplo de cómo usar algunos de estos métodos de aserción en una prueba unitaria:

```py
class MyTestCase(unittest.TestCase):
    def test_math(self):
        # Verificar la suma
        self.assertEqual(1 + 2, 3)

        # Verificar la resta
        self.assertEqual(5 - 2, 3)

        # Verificar la multiplicación
        self.assertEqual(2 * 3, 6)

        # Verificar la división
        self.assertEqual(6 / 2, 3)

        # Verificar si una cadena está en otra
        self.assertIn('hello', 'hello world')

        # Verificar si se produce una excepción
        self.assertRaises(ZeroDivisionError, lambda: 1 / 0)
```

En este ejemplo, definimos un método de prueba test_math() que realiza varias pruebas unitarias utilizando diferentes métodos de aserción. La prueba verifica la suma, la resta, la multiplicación y la división de números, y también verifica si una cadena está contenida en otra. La última prueba utiliza el método assertRaises() para verificar si se produce una excepción de división por cero al ejecutar una operación de división por cero.

Además de los métodos de aserción, la biblioteca unittest también proporciona una serie de métodos para configurar y limpiar las pruebas, así como para agrupar y ejecutar pruebas de manera más efectiva. Algunos de estos métodos incluyen:

setUp(): se ejecuta antes de cada prueba y se utiliza para configurar el entorno de prueba.
tearDown(): se ejecuta después de cada prueba y se utiliza para limpiar el entorno de prueba.
setUpClass(): se ejecuta una vez al inicio de la ejecución de todas las pruebas y se utiliza para configurar el entorno de prueba a nivel de clase.
tearDownClass(): se ejecuta una vez al final de la ejecución de todas las pruebas y se utiliza para limpiar el entorno de prueba a nivel de clase.
skip(reason): se utiliza para omitir una prueba y se puede proporcionar una razón opcional para la omisión.
A continuación, se muestra un ejemplo de cómo usar algunos de estos métodos en una clase de prueba:

```py
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar el entorno de prueba a nivel de clase
        pass

    def setUp(self):
        # Configurar el entorno de prueba
        pass

    def test_addition(self):
        # Verificar la suma
        self.assertEqual(1 + 2, 3)

    @unittest.skip("Esta prueba está desactivada temporalmente")
    def test_subtraction(self):
        # Verificar la resta
        self.assertEqual(5 - 2, 3)

    def tearDown(self):
        # Limpiar el entorno de prueba
        pass

    @classmethod
    def tearDownClass(cls):
        # Limpiar el entorno de prueba a nivel de clase
        pass
```

En este ejemplo, definimos una clase de prueba MyTestCase que utiliza los métodos setUp(), tearDown(), setUpClass() y tearDownClass() para configurar y limpiar el entorno de prueba. También utilizamos el método skip() para omitir temporalmente una prueba de resta.

En resumen, unittest es una biblioteca de Python que se utiliza para escribir y ejecutar pruebas unitarias. Permite definir pruebas unitarias utilizando diferentes métodos de aserción y proporciona métodos para configurar y limpiar el entorno de prueba. unittest es una herramienta esencial para garantizar la calidad del código y reducir los errores en proyectos de Python.

se puede decir que unittest es solo una de las muchas bibliotecas de pruebas disponibles en Python. Otras bibliotecas populares incluyen pytest, doctest y nose. Cada biblioteca tiene sus propias características y ventajas, por lo que es importante investigar y encontrar la que mejor se adapte a las necesidades de cada proyecto.

La biblioteca pytest, por ejemplo, es conocida por su sintaxis más simple y sus capacidades de informes más detallados. También tiene una gran cantidad de complementos y extensiones disponibles que pueden mejorar aún más su funcionalidad. Por otro lado, la biblioteca doctest se utiliza para escribir pruebas dentro de la documentación del código, lo que lo hace ideal para proyectos con una documentación extensa.

Además, la página web proporciona información sobre cómo escribir pruebas eficaces, incluyendo el uso de casos de prueba de borde y pruebas de cobertura de código. También se proporciona información sobre cómo automatizar las pruebas mediante herramientas como Jenkins y Travis CI.

En resumen, la página web proporciona información valiosa sobre cómo escribir pruebas unitarias en Python utilizando la biblioteca unittest, así como información sobre otras bibliotecas de pruebas populares y cómo escribir pruebas eficaces en general. La página también cubre la automatización de pruebas, lo que es importante para proyectos más grandes y complejos.

</details>

</details>


<details>
<summary><h2>detalles</h2></summary>

```py
del - operador para borrar datos en la memoria
ejemplo
nombre = "sapito"
del nombre
"""se borro la variable en la memoria"""
```
esto va por oreden de lectura por ejemplo:

```py
nombre = "sapito"
completo = f"{nombre}rico" - la seccion donde esta nombre ya adquirio el valor de la variable ya creado completo.
del nombre
print(completo)
output: sapitorico
```

</details>

# Recrusos

<iframe src="https://overapi.com/python" width="100%" height="400px"></iframe>



<p>Este repsoitorio esta dedicadoa mi estudio y desarrollo con el lengruaje python</p>
