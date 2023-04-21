https://rogerdudler.github.io/git-guide/index.es.html

# Inicializacion de un repositorio Git

## Creacion de repositorio local

```
git init
```

## Vinculacion con repositorio remoto github

```
git remote add origin <REMOTE_URL>
```

## Traemos lo que esta en repositorio remoto al working directory (local)

```
git pull origin main
```

## Verificacion URL remota

```
git remote -v
```

## Chequeo de status del working directory

```
git status
```

## Agregar cambios locales al stage

```
git add .
```

## Creacion de commit

Mediante consola

```
git commit
```
o

```
git commit -m 'Mensaje'
```

## Cambio de nombre de rama de Master a Main si no se crea como main

```
git branch -m master main
```

## Primer Push

```
git push --set-upstream origin main
```


En caso de que aparezca algo como lo siguiente
```
origin  git@github.com:fedepacher/Prueba_git.git (fetch)
origin  git@github.com:fedepacher/Prueba_git.git (push)
```
quiere decir que hay que hacer un fetch (buscar y traer cambios)
```
git fetch origin main
```
```
git push origin main
```
en caso del siguiente error
```
! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'git@github.com:fedepacher/Prueba_git.git'
```
```
git push -ff origin main
```

## Luego del primer push solo basta con utilizar el push de la siguiente forma

```
git push
```


## Creacion de una nueva rama

```
git checkout -b nombre_rama
```

> Note: -b crea la rama si no existe. si la rama existe se puede utilizar git checkout nombre_rama

## Chequeo de ramas

```
git branch
```

## Eliminamos la rama X en local

```
git branch -d nombre_rama
```

## Para saber los branch en remoto

```
git branch -a
```

## Para eliminar el branch en remoto

```
git push origin -d branch_X
```

## Pushear cambios a la nueva rama (luego de pushear se vera reflejado en local y en remoto)

```
git add .
git commit -m 'mensaje'
git push --set-upstream origin nombre_rama
```

## Chequeo diferencias entre ramas

```
git diff nombre_rama
```

## Chequeo de historial de log

- Multiples lineas
```
git log
```

- Una sola linea
```
git log --oneline
```

### Grafico de branches

```
git log --graph
```

Con mejor descripcion
```
git log --all --decorate --oneline --graph
```

## Para actualizar tu repositorio local al commit más nuevo

```
git pull
```

## Merge: Para fusionar otra rama a tu rama activa (por ejemplo master)

Estando en la rama X me traigo los cambios de main por si esto han cambiado (no deberia ya que en main no se trabaja pero pudo haber cambios ingresados desde otras ramas)

```
git merge branch_X
```

Hace el merge con la rama branch_X.

Luego del merge es necesario hacer el push al remoto.

```
git push
```

# Creacion de Tags

```
git tag "vX.X.X"
git push origin --tags
```

# Traigo los cambios de main para colocarlos en mi rama asi la mantenngo actualizada

- Busco cambios

```
git fetch
```

Traigo cambios

```
git pull origin main
```

Resulevo conflictor y hago commit.

Por otro lado, si quieres deshacer todos los cambios locales y commits, puedes traer la última versión del servidor y apuntar a tu copia local principal de esta forma

```
git fetch origin
```
```
git reset --hard origin/main
```

# Traigo las ramas del remoto que no tengo en mi local

```
git fetch
```
```
git pull origin <Nombre de la rama>
```

# Resetear/borrar el ultimo commit local

```
git reset --hard HEAD~1
```

Luego actualizamos el remoto

```
git push origin +HEAD
```