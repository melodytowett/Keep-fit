import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

import { HttpHeaders } from '@angular/common/http';



import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-trainee-sign-up',
  templateUrl: './trainee-sign-up.component.html',
  styleUrls: ['./trainee-sign-up.component.css']
})
export class TraineeSignUpComponent implements OnInit {

  email :string = ''
  username: string = '';
  password: string = '';

  url: string = environment.API_URL + 'trainee/signup';

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTraineeSignUp() {
    this.router.navigate(['trainee-sign-up'])
  }

  ngOnInit(): void {
  }

  signupTrainee() {

    const body = {
      email: this.email,
      username: this.username,
      password: this.password
    }
    

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })};

    let response:any={}



    this.http.post(this.url, body, httpOptions).subscribe(data=>{
      response = data
      if (response.status == 'success') {
        this.router.navigate(['/login-trainer']);
      }else{
        alert(response.message)
      }
    })
  }

}
