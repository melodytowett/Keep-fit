import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainerCreateGigComponent } from './trainer-create-gig.component';

describe('TrainerCreateGigComponent', () => {
  let component: TrainerCreateGigComponent;
  let fixture: ComponentFixture<TrainerCreateGigComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainerCreateGigComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainerCreateGigComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
