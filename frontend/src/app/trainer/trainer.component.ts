import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';


import { environment } from 'src/environments/environment';
import { Gig } from '../gig';

@Component({
  selector: 'app-trainer',
  templateUrl: './trainer.component.html',
  styleUrls: ['./trainer.component.css']
})
export class TrainerComponent implements OnInit {

  url: string = environment.API_URL ;
  gigs: Gig[];
  gig = Gig;


  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTrainer() {
    this.router.navigate(['trainer'])
  }
  ngOnInit(): void {

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })};

    let response:any={}

    this.http.get(this.url, httpOptions).subscribe(data=>{
      response = data
      this.gigs = response

    })
  }

}
