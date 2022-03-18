import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainerSignUpComponent } from './trainer-sign-up.component';

describe('TrainerSignUpComponent', () => {
  let component: TrainerSignUpComponent;
  let fixture: ComponentFixture<TrainerSignUpComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainerSignUpComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainerSignUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
