import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-inicio-sesion',
  templateUrl: './inicio-sesion.page.html',
  styleUrls: ['./inicio-sesion.page.scss'],
})
export class InicioSesionPage implements OnInit {

  usuario = {
    correo: '',
    password: ''
  };

  constructor() { }

  ngOnInit() {
  }

  onSubmitTemplate(){
    console.log('Form submit');
  }

}
