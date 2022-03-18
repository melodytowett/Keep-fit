import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-trainee-sign-up',
  templateUrl: './trainee-sign-up.component.html',
  styleUrls: ['./trainee-sign-up.component.css']
})
export class TraineeSignUpComponent implements OnInit {

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTraineeSignUp() {
    this.router.navigate(['trainee-sign-up'])
  }

  ngOnInit(): void {
  }

}
