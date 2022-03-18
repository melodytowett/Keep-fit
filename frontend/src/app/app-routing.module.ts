import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TrainerComponent } from './trainer/trainer.component';
import { TraineeComponent } from './trainee/trainee.component';
import { HomeComponent } from './home/home.component';
import { CreateGigComponent } from './create-gig/create-gig.component';
import { ViewGigsComponent } from './view-gigs/view-gigs.component';
import { DisplayGigComponent } from './display-gig/display-gig.component';
import { TraineeLoginComponent } from './login/trainee-login/trainee-login.component';
import { TrainerLoginComponent } from './login/trainer-login/trainer-login.component';
import { TrainerSignUpComponent } from './sign-up/trainer-sign-up/trainer-sign-up.component';
import { TraineeSignUpComponent } from './sign-up/trainee-sign-up/trainee-sign-up.component';

const routes: Routes = [
  { path: 'trainer', component: TrainerComponent },
  { path: 'trainee', component: TraineeComponent },
  { path: 'home', component: HomeComponent },
  { path: 'create-gig', component: CreateGigComponent },
  { path: 'view-gigs', component: ViewGigsComponent },
  { path: 'display-gig/:id', component: DisplayGigComponent },
  { path: 'trainer-login', component: TrainerLoginComponent},
  { path: 'trainee-login', component: TraineeLoginComponent},
  { path: 'trainer-sign-up', component: TrainerSignUpComponent},
  { path: 'trainee-sign-up', component: TraineeSignUpComponent},
  { path: '', component: HomeComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
