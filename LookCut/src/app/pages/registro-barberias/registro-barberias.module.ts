import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { RegistroBarberiasPageRoutingModule } from './registro-barberias-routing.module';

import { RegistroBarberiasPage } from './registro-barberias.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RegistroBarberiasPageRoutingModule
  ],
  declarations: [RegistroBarberiasPage]
})
export class RegistroBarberiasPageModule {}
