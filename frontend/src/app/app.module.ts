import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavigationBarComponent } from './navigation-bar/navigation-bar.component';

import { FormsModule } from '@angular/forms';
import { FooterComponent } from './footer/footer.component';
import { TrainerComponent } from './trainer/trainer.component';
import { TraineeComponent } from './trainee/trainee.component';
import { HomeComponent } from './home/home.component';
import { CreateGigComponent } from './create-gig/create-gig.component';
import { ViewGigsComponent } from './view-gigs/view-gigs.component';
import { DisplayGigComponent } from './display-gig/display-gig.component';


@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    FooterComponent,
    TrainerComponent,
    TraineeComponent,
    HomeComponent,
    CreateGigComponent,
    ViewGigsComponent,
    DisplayGigComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule, 
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
