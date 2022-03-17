import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

import { environment } from 'src/environments/environment';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-signup-trainer',
  templateUrl: './signup-trainer.component.html',
  styleUrls: ['./signup-trainer.component.css']
})
export class SignupTrainerComponent implements OnInit {

  email :string = ''
  username: string = '';
  phone_number: string = '';
  password: string = '';
  url: string = environment.API_URL + 'trainer/signup';

  constructor(private readonly http: HttpClient, private router: Router) {}

  ngOnInit(): void {
  }


  signupTrainer() {
    const body = {
      email: this.email,
      username: this.username,
      phone_number: this.phone_number,
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
      }
      
      
    })
  }

}
