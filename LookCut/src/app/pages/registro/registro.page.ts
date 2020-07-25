import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.page.html',
  styleUrls: ['./registro.page.scss'],
})
export class RegistroPage implements OnInit {

  registro = {
    nombres: '',
    telefono: '',
    correo: '',
    contrasenia: '',
    confirmContrasenia: '',
    tipoCliente: ''
  };

  constructor() {}

  ngOnInit() {}

  onSubmitForm() {
    console.log('Form submit');
  }
}
