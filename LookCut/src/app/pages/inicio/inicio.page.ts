import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.page.html',
  styleUrls: ['./inicio.page.scss'],
})
export class InicioPage implements OnInit {
  logo = [
    {
      image: 'assets/imgs/logo.jpg',
      title: 'LookCut',
    },
  ];

  constructor() {}

  ngOnInit() {}
}
