import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TraineeSignUpComponent } from './trainee-sign-up.component';

describe('TraineeSignUpComponent', () => {
  let component: TraineeSignUpComponent;
  let fixture: ComponentFixture<TraineeSignUpComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TraineeSignUpComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TraineeSignUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
