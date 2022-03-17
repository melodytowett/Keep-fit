import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SignupTraineeComponent } from './auth/signup-trainee/signup-trainee.component';
import { SignupTrainerComponent } from './auth/signup-trainer/signup-trainer.component';
import { LoginTraineeComponent } from './auth/login-trainee/login-trainee.component';
import { LoginTrainerComponent } from './auth/login-trainer/login-trainer.component';
import { TrainerCreateGigComponent } from './trainer/trainer-create-gig/trainer-create-gig.component';


const routes: Routes = [
  { path: 'login-trainee', component: LoginTraineeComponent },
  { path: 'login-trainer', component: LoginTrainerComponent },
  { path: 'signup-trainee', component: SignupTraineeComponent },
  { path: 'signup-trainer', component: SignupTrainerComponent },
  {path: 'create-gig', component: TrainerCreateGigComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
