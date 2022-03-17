import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginTraineeComponent } from './auth/login-trainee/login-trainee.component';
import { LoginTrainerComponent } from './auth/login-trainer/login-trainer.component';
import { SignupTrainerComponent } from './auth/signup-trainer/signup-trainer.component';
import { SignupTraineeComponent } from './auth/signup-trainee/signup-trainee.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginTraineeComponent,
    LoginTrainerComponent,
    SignupTrainerComponent,
    SignupTraineeComponent
  ],
  imports: [
    HttpClientModule,
    FormsModule,
    BrowserModule,
    AppRoutingModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
