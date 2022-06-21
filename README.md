# kut1t!

* Alexis Rodríguez Casañas
* 21/06&2022

Kut1t (pronuncidado *cut it!*) es un acortador de enlaces responsivo que funciona tanto en PC coomo en tablet o móvil.

![](https://github.com/alexrcas/kut1t/blob/master/example.gif)

Kut1t transforma enlaces como el siguiente:
```
https://unaweb.enlace.realmente.largo-en-un-lugar-la-mancha?author=cervantes&protagonista=donquijote
```
Devolviendo un resultados como este:
```
https://kut1t.com/QeT
```
Este enlace funciona igual que el original pero ocupa un menor espacio, mejorando la legibilidad o ahorrando espacio cuando sea necesario, como por ejemplo, en un tweet.

### Tecnologías

* Backend: Python (Flask)
* Front-end: Vue 3 + Bootstrap 5

### Otras consideraciones
* Función de copiado al portapapeles
* En su versión para PC, ofrece un pequeño historial que almacena localmente los 5 últimos enlaces acortados.
