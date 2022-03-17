import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginTraineeComponent } from './login-trainee.component';

describe('LoginTraineeComponent', () => {
  let component: LoginTraineeComponent;
  let fixture: ComponentFixture<LoginTraineeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginTraineeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginTraineeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
