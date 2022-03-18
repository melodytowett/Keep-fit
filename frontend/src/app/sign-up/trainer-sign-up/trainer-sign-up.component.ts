import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-trainer-sign-up',
  templateUrl: './trainer-sign-up.component.html',
  styleUrls: ['./trainer-sign-up.component.css']
})
export class TrainerSignUpComponent implements OnInit {

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTraineeSignUp() {
    this.router.navigate(['trainee-sign-up'])
  }

  ngOnInit(): void {
  }

}
