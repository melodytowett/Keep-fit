import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

import { HttpHeaders } from '@angular/common/http';



import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-trainer-sign-up',
  templateUrl: './trainer-sign-up.component.html',
  styleUrls: ['./trainer-sign-up.component.css']
})
export class TrainerSignUpComponent implements OnInit {


  email :string = ''
  username: string = '';
  password: string = '';
  phone_number:string=''

  url: string = environment.API_URL + 'trainer/signup';

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTraineeSignUp() {
    this.router.navigate(['trainee-sign-up'])
  }

  ngOnInit(): void {
  }

  signupTrainer() {
    const body = {
      email: this.email,
      username: this.username,
      password: this.password,
      phone_number : this.phone_number
    }
    
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })};

    let response:any={}

    this.http.post(this.url, body, httpOptions).subscribe(data=>{
      response = data
      if (response.status == 'success') {
        this.router.navigate(['/trainer-login']);
      }else{
        alert(response.message)
      }
    })
  }

}
