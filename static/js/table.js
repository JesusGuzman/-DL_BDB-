var datos = [
 {
 "id": "1",
 "nombres": "MARIA",
 "apellidos": "RUIZ"
 },
 {
 "id": "2",
 "nombres": "KARL",
 "apellidos": "MARX"
 },
 {
 "id": "3",
 "nombres": "BILL",
 "apellidos": "GATES"
 },
 {
 "id": "4",
 "nombres": "LOLA",
 "apellidos": "LIZ"
 }
];

var d = '<tr>'+
'<th>ID</th>'+
'<th>Nombres</th>'+
'<th>Apellidos</th>'+
'</tr>';

$("#btnCargar").click(function () {
 for (var i = 1; i < datos.length; i++) {
 d+= '<tr>'+
 '<td>'+datos[i].id+'</td>'+
 '<td>'+datos[i].nombres+'</td>'+
 '<td>'+datos[i].apellidos+'</td>'+
 '</tr>';
 }
 $("#tabla").append(d);
});
