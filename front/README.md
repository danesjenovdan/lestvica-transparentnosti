# lestvica-transparentnosti

## Build Setup

### Environment

```bash
# copy example .env and modify it
$ cp .env.example .env
```

### Run
```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev

# build for production and launch server
$ yarn build
$ yarn start

# generate static project
$ yarn generate
```


---

## Optimizacija svg zemljevida občin

Zemljevid lociran v [map.svg](./assets/images/map.svg) je ročno optimizirana verzija svg datoteke iz [Wikipedije](https://sl.wikipedia.org/wiki/Slika:Obcine_Slovenija_2006.svg).

Proces optimizacije je bil kombinacija sprememb v programu Inkscape in optimizaciji preko [svgomg](https://jakearchibald.github.io/svgomg/).

Ker sta simplifikacija in optimizacija lahko destruktivna procesa in zelo odvisna od prejšnjega stanja to ni 100% vodič, ampak samo približen popis korakov kako sem prišel do trenutne optimizirane verzije.

**Če hočeš da se v tem procesu ne izgubijo attributi imen občin svg tagih, je treba med vsakim korakom preverit in/ali popravit da so imena podvojena za vsako občino v `id="<ime>"` in `data-name="<ime>"`, ker se lahko pri različnih korakih odvisno od tega katera optimizacija se naredi eden ali drug izgubi.**

Približni koraki so bili:
1. Inkscape: scale down na 1%
2. Inkscape: scale down na 50%
3. Inkscape: Resize document to selection
4. svgomg: optimizacija (precision: 2)
5. Inkscape: Simplify (pazi da ne klikneš večkrat ker je zelo agresiven)
6. svgomg: optimizacija (precision: 2)
