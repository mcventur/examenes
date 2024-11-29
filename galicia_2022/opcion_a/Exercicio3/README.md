# EXERCICIO 3 (2 puntos) 
Un administrador de sistemas informáticos debe saber explotar os Sistemas Xestores de Bases de Datos. 
Deberá levar a cabo unha serie de tarefas de administración sobre o sistema de base de datos MySQL que 
teñen implementado nunha determinada empresa (sabendo que é unha versión 5.7 ou superior e cun 
sistema Windows). Conteste ás seguintes cuestións: 

Supoña que iniciou sesión como root e polo tanto, está traballando co cliente mysql a través da liña de 
comandos.  

a) O servidor mantén diferentes variables de estado que proporcionan información sobre as 
operacións levadas a cabo. Que variable permite coñecer o número de intentos de conexión 
erróneos ao servidor MySQL? 

<font color="grey">
Resposta: 

O servidor mysql ten unha serie de variables de estado que se poden consultar con 
SHOW GLOBAL STATUS; A que nos interesa é *Aborted_connects*.

```shell
SHOW GLOBAL STATUS LIKE 'Aborted_connects';
```
Pódense consultar outras variables na [documentación oficial](https://dev.mysql.com/doc/refman/8.4/en/server-status-variables.html).
</font>

Supoña que de aquí en adiante estará situado no prompt do sistema. 

b) O sitio web que xestionamos aumentou considerablemente o número de visitas por parte dos usuarios, os cales fan uso das conexións á nosa base de datos  MySQL e debido a iso xéranse tamén erros. Unha posible solución sería aumentar o número de conexións abertas ao mesmo tempo. Indique o comando a executar dende a consola de Windows para establecer o número de conexións en 200 para o noso servidor MySQL e que ese cambio sexa permanente. 

<font color="grey">
Resposta: 

Para que os cambios en variables de sistema sexan permanentes, a partir de mysql 8.0, permítese usar o modificador *PERSIST* co comando SET. O enunciado indica que a versión de mysql é 5.7 **ou posterior**. Se o tribunal admite a 8.0 dentro desta descripción entón a resposta sería esta. 

```shell
SET PERSIST max_connections = 1000;
```

Antes da versión 8.0, para modificar permanentemente estas variables non había outra que editar o arquivo my.ini, modificando o valor da directiva max_connections, e reiniciar o servizo mysql. 
</font>

c) Cal é a variable do sistema que permite a un usuario de  MySQL conectarse ao servidor dende calquera dirección IP que non sexa a dirección local? Indique cal é o proceso a seguir para que permita conectarse dende outras direccións IP ao servidor MySQL. 

<font color="grey">
Resposta:

```shell
SET GLOBAL bind_address = '*'
```
Neste caso, o valor non sería permanente, pero tampoco se pide. 
[Máis info](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_bind_address)
</font>

d) Hai que levar a cabo a realización dunha copia de seguridade das táboas Cliente e Proveedor que pertencen á base de datos Suministros e que se gardarán nun arquivo chamado “Copia_003. sql”. 

Escriba a sintaxe correcta para realizar dita copia.

<font color="grey">
Resposta:

Para exportar bases de datos ou táboas, dende fora da shell de mysql, úsase o comando mysqldump, indicando a base de datos e as táboas separadas por espacios:
```shell
mysqldump -u root -p Suministros Cliente Proveedor > Copia_003.sql
```
</font>

e) Cree un novo usuario “invitado”, de uso temporal, para acceder ao servidor. Dito usuario só terá acceso dende o equipo con  IP  192.168.100.100, e chave “invitado01”  que debe cambiar cada 15 días. 

Ademais, habilite o seguimento dos inicios de sesión erróneos que tivese, de tal xeito que se teñen lugar 3 intentos de acceso incorrectos bloquearase temporalmente a conta durante 2 días. 

<font color="grey">
Resposta:
Para crear o usuario coas restricción indicadas, dende unha shell mysql con privilegios, executamos:

```shell
mysql> CREATE USER 'invitado'@'192.168.100.100' IDENTIFIED BY 'invitado01' PASSWORD EXPIRE INTERVAL 15 DAY FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
```
</font>

f) O usuario “invitado” terá permisos para seleccionar datos e inserir rexistros na táboa Cliente. Na táboa Proveedor só poderá modificar os campos telefono e direccion, e ver o nome. Ambas táboas pertencen á base de datos Suministros. 

<font color="grey">

Resposta:

```shell
#Permiso para SELECT e INSERT na táboa Cliente
mysql> GRANT SELECT, INSERT ON Suministros.Cliente TO 'invitado'@'192.168.1.129';

#Permiso para Select do campo nome, e modificar telefono e direccion na táboa Proveedor. 
mysql> GRANT SELECT(nome), UPDATE(telefono, direccion) ON Suministros.Proveedor TO 'invitado'@'192.168.1.129';
```
</font>
g) Cree unha vista chamada “v1” que permita seleccionar todos os rexistros da táboa Cliente onde a deuda sexa inferior a 150€, de xeito que as insercións que se fagan posteriormente a través desta vista, deberán ser verificadas previamente.

<font color="grey">
Reposta:

```java
/*
wITH CHECK OPTION obliga a que calquera modificación ou inserción
feita a partires da vista, cumpla a condición establecida no WHERE
*/
CREATE VIEW V1 as
    SELECT * FROM Cliente WHERE deuda < 150;
WITH CHECK OPTION 
```
</font>





