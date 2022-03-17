import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SignupTraineeComponent } from './signup-trainee.component';

describe('SignupTraineeComponent', () => {
  let component: SignupTraineeComponent;
  let fixture: ComponentFixture<SignupTraineeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SignupTraineeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SignupTraineeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
