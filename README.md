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
 - image_path: /img/slider/nom_de_la_foto.extensio
   gallery-folder: /img/slider/
```

#### Esborrar imatge de l'animació.

Per esborrar la imatge només has de treure la entrada en questió al fitxer [index.html](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/index.html) i esborrar el fitxer de la carpeta (Obrint el fitxer primer i després clicant a "esborrar")

### Gallery

L'estructura de la galería és la seguent:

- [Albums](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/gallery/albums) conté les fotos que vols que surtin com a "portada" dels àlbums a la pàgina principal.
- [Archive](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/gallery/archive) conté totes les imatges de la galería. Preferiblement organitzades per album.
- Una carpeta per cada album que es mostri. Preferiblment amb un nom \*gallery*nom_album*).
- [Index.html](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/gallery/index.html) amb la pàgina principal. \*\*Ullet que és diferent al primer index.html

#### Afegir Album

Primer de tot has de crear una nova carpeta amb nom "gallery_nom_del_album" a la carpeta [gallery](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/gallery). També necessites una nova carpeta amb el mateix nom però dins de la carpeta [archive](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/gallery/archive).

Segon, puja totes les fotos del nou album dins de la nova carpeta a archive. També puja la fote vols que surti com a miníatura dins de la carpeta [albums](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/gallery/albums) (enrecorda't ddel nom).

Copia el contingut del fitxer [plantilla](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/gallery/gallery_plantilla/index.html) dins de la nova carpeta creada a gallery. Canvia els valors que necessitis i per cada imatge pujada has de posar una nova entrada.

Finalment has de modificar el fitxer [gallery/index.html](https://github.com/marcgarnica13/ariadnevenzal/blob/gh-pages/gallery/index.html) on tens la pàgina principal de la galería.

Per cada album que vulguis has tenir necessites una entrada especificant la foto en miniatura, la carpeta de la galería, nom i data.

```
 - image_path: gallery/albums/nom_foto_miniatura.extensió
   gallery-folder: gallery/gallery_nom_album/
   gallery-name: nom_album
   gallery-date: data_album
```

#### Afegir un Post

Per afegir un post només has de pujar un nou fitxer a la carpeta [posts](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/_posts) amb la següent estructura:

```
---
layout: post
title: "Titol"
subtitle: "Subtitol"
active: journal
image:
  feature: "nom_miniatura.jpg"
date: 2020-12-24
header-img: "img/postcover/post_primer.jpg"
tags: []
categories: []
comments: false
---

<Contingut del post>
```

La foto "nom_miniatura.jpg" ha d'estar dins de la carpeta de [portades de post](https://github.com/marcgarnica13/ariadnevenzal/tree/gh-pages/img/postcover)

Based on [Photorama](https://raw.githubusercontent.com/sunbliss/photorama)
And **jekyll**
