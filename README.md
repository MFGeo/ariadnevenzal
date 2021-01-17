# Personal webpage

## Configuració general

Tota la configuració general de la pàgina la pots trobar al fitxer [\_config.yml](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/_config.yml)

És on tota la "magia" passa però és útil per canviar:

- Titol de la pàgina (que surt com a nom de la pestanya).
- Email.
- Descripció
- URL (ojito)
- Usuari facebook o Instagram (o altres).
- Estructura de la web (això és una mica més complicat que canviar-ho solament aqui)

## Estructura de la pàgina

La pàgina de moment només té **4 grans apartats**:

- [index.html](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/index.html): És la pàgina d'inici.
- La carpeta [journal](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/journal) per tots els posts amb la [\_posts](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/_posts) pel contingut de cadascún.
- La carpeta [gallery](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/gallery) per la galeria de fotos.
- La carpeta [about](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/about) per l'apartat "Sobre mi".
- Totes les imatges (galería, sobre mi, posts) estan ordenades a la carpeta [img](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/img)

## Receptes

### Pàgina principal: Info + Animació

Per canviar la info que es mostra a la pàgina principal només has de tenir present el primer apartat (entre '---') del fitxer [index.html](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/index.html).

L'animació és automàtica i només "li has d'indicar" a la web quines imatges utilitzar. Et recomano mantenir les imatges de la animació en una carpeta dins de la carpeta de img: [slider](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/img/slider).

#### Afegir imatge a l'animació

- Navega a la carpeta [slider](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/img/slider).
- Clica a "afegir fitxer" i "puja".
- Selecciona el fitxer en questió.
- Afegeix una nova entrada dins de l'apartat "images" del [index.html](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/index.html). La nova entrada hauria de ser similar a:

```
image_path: /img/slider/nom_de_la_foto.extensio
gallery-folder: /img/slider/
```

#### Esborrar imatge de l'animació.

Per esborrar la imatge només has de treure la entrada en questió al fitxer [index.html](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/index.html) i esborrar el fitxer de la carpeta (Obrint el fitxer primer i després clicant a "esborrar")

Based on [Photorama](https://raw.githubusercontent.com/sunbliss/photorama)
And **jekyll**
