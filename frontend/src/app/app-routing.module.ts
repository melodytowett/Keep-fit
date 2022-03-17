import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TrainerComponent } from './trainer/trainer.component';
import { TraineeComponent } from './trainee/trainee.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  { path: 'trainer', component: TrainerComponent },
  { path: 'trainee', component: TraineeComponent },
  { path: 'home', component: HomeComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
