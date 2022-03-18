import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-trainer-login',
  templateUrl: './trainer-login.component.html',
  styleUrls: ['./trainer-login.component.css']
})
export class TrainerLoginComponent implements OnInit {

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTrainerLogin() {
    this.router.navigate(['trainer-login'])
  }

  ngOnInit(): void {
  }

}
