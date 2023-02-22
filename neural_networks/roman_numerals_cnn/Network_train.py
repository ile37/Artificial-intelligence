from Network_model import *
import torch.optim as optim
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import sys

"""
If want to save model parameters use command line argument 'sava'
"""

def main():

    args = sys.argv[1:]

    # Get train and test dataloaders
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5], std=[0.5])
    ])

    # Load the dataset using ImageFolder
    train_dataset = datasets.ImageFolder(r'D:\coding projects\Neural Networks\Roman numerals\images\train', transform=transform)
    test_dataset = datasets.ImageFolder(r'D:\coding projects\Neural Networks\Roman numerals\images\val', transform=transform)

    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=2)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=32, shuffle=False, num_workers=2)

    # Set up the model, loss function, and optimizer
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = Net().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.005, momentum=0.9)

    # Train the model
    for epoch in range(50):
        train_loss = train(model, train_loader, criterion, optimizer, device)
        print(f"Epoch {epoch+1}, training loss: {train_loss:.3f}")

    # Evaluate the model
    test_loss, test_acc = evaluate(model, test_loader, criterion, device)
    print(f"Test loss: {test_loss:.3f}, test accuracy: {test_acc:.3f}")

    if len(args) > 0:
        if args[0] == 'save':
            # Save the model parameters to a file
            torch.save(model.state_dict(), 'save\model_params.pth')
            print("model saved")
        else:
            print("model NOT saved")
    else:
        print("model NOT saved")


if __name__ == "__main__":
    main()