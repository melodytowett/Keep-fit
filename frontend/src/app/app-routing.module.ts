import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TrainerComponent } from './trainer/trainer.component';
import { TraineeComponent } from './trainee/trainee.component';
import { HomeComponent } from './home/home.component';
import { CreateGigComponent } from './create-gig/create-gig.component';
import { ViewGigsComponent } from './view-gigs/view-gigs.component';
import { DisplayGigComponent } from './display-gig/display-gig.component';

const routes: Routes = [
  { path: 'trainer', component: TrainerComponent },
  { path: 'trainee', component: TraineeComponent },
  { path: 'home', component: HomeComponent },
  { path: 'create-gig', component: CreateGigComponent },
  { path: 'view-gigs', component: ViewGigsComponent },
  { path: 'display-gig/:id', component: DisplayGigComponent },


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
